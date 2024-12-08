import os
import numpy as np

import scipy.io as sio

# set contstants
FS = 128 # Hz

SEC_SEG = 20 # second
LEN_SEG = FS * SEC_SEG # number of time steps

SEC_DIS = 1  # second (discarded)
LEN_DIS = FS * SEC_DIS # number of time steps (discarded)

def segmentation(dir_path_load: str, dir_path_save: str):
    os.makedirs(dir_path_save, exist_ok=True)

    for file_name in os.listdir(dir_path_load):
        if not file_name.endswith('.mat'):
            print(f"'{file_name}' is invalid")
            continue

        file_path = os.path.join(dir_path_load, file_name)
        mat_dictionary = sio.loadmat(file_path)
        
        # get key & sbj & x
        key = os.path.splitext(file_name)[0]
        sbj = key.split('_')[0]
        x = mat_dictionary[key].astype(np.float32)
        
        # x (start-discarded)
        x = x[LEN_DIS:, :]

        # x (end-discarded)
        num_segments = x.shape[0] // LEN_SEG 
        x = x[: num_segments * LEN_SEG:, :]

        # segment x
        segments = np.array_split(x, num_segments)
        
        for seq, segment in enumerate(segments, start = 1):
            file_path_save = os.path.join(dir_path_save, f"{sbj}_{seq}.mat")
            sio.savemat(file_path_save, {f"{sbj}_{seq}": segment})