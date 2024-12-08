import os
import numpy as np

import scipy.io as sio
from scipy.signal import welch

# set contstants
FS = 128 # Hz

NUM_CHANNEL = 19
NUM_F = 64

def PSD(dir_path_load: str, dir_path_save: str):
    os.makedirs(dir_path_save, exist_ok=True)

    for file_name in os.listdir(dir_path_load):
        if not file_name.endswith('.mat'):
            print(f"'{file_name}' is invalid")
            continue

        file_path = os.path.join(dir_path_load, file_name)
        mat_dictionary = sio.loadmat(file_path)
        
        # get key & x
        key = os.path.splitext(file_name)[0]
        x = mat_dictionary[key].astype(np.float32)
        
        # return value initialization
        psd = []

        # get psd of each channel
        for channel in range(NUM_CHANNEL):
            x_channel = x[:, channel]
            _, psd_channel = welch(x_channel, fs=FS, nperseg=FS)
            psd.append(psd_channel[:NUM_F])
        
        # set psd
        psd = np.array(psd).astype(np.float32)

        # save psd(x)
        file_path_save = os.path.join(dir_path_save, f"{key}.mat")
        sio.savemat(file_path_save, {f"{key}": psd})