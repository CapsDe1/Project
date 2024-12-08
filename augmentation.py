import numpy as np
import os

import scipy.io as sio

def augmentation(dir_path_load:str, dir_path_save: str,
    scale_factor=0.8, 
    noise_level=0.005, 
    shift_range=3, 
    band_factor=1.1, 
    band_range=(10, 13), 
    augmentation_methods=['scaling', 'noise', 'shift', 'band_emphasis']
):
    os.makedirs(dir_path_save, exist_ok=True)

    for file_name in os.listdir(dir_path_load):
        if not file_name.endswith('.mat'):
            print(f"'{file_name}' is invalid")
            continue

        file_path = os.path.join(dir_path_load, file_name)
        mat_dictionary = sio.loadmat(file_path)
        
        # get key & sbj & x
        key = os.path.splitext(file_name)[0]
        x = mat_dictionary[key].astype(np.float32)

        if 'scaling' in augmentation_methods:
            x *= scale_factor

        if 'noise' in augmentation_methods:
            noise = np.random.normal(0, noise_level, x.shape)
            x += noise

        if 'shift' in augmentation_methods:
            shift = np.random.randint(-shift_range, shift_range + 1)
            x = np.roll(x, shift, axis=0)

        if 'band_emphasis' in augmentation_methods:
            band_start, band_end = band_range
            x[band_start:band_end] *= band_factor

        x = x.astype(np.float32)

        file_path_save = os.path.join(dir_path_save, f"{key}.mat")
        sio.savemat(file_path_save, {f"{key}": x})