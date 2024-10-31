import os

import numpy as np

import scipy.io as sio

def save_segments_mat(dir_path: str, save_dir_path: str, fs: int, seg_second: int, discarded_second: int):
    os.makedirs(os.path.join(save_dir_path), exist_ok=True)

    samples_num_per_seg = seg_second * fs
    discarded_samples_num = discarded_second * fs

    for file_name in os.listdir(dir_path):
        if file_name.endswith('.mat'):
            file_path = os.path.join(dir_path, file_name)
            key = os.path.splitext(file_name)[0] 
            mat_data = sio.loadmat(file_path)

            data = mat_data[key]

            data = data[discarded_samples_num:, :]

            data = data.astype(np.float64)
        
            samples_num_per_channel = data.shape[0]
            seg_num = samples_num_per_channel // samples_num_per_seg
            
            data = data[:seg_num * samples_num_per_seg, :]

            segs = np.array_split(data, seg_num)

            for number, seg in enumerate(segs, start = 1):
                print(f"segment {number} from {key}: Shape = {seg.shape}, Size = {seg.size}")
                
                save_file_path = os.path.join(save_dir_path, f"{key}_seg{number}.mat")
                sio.savemat(save_file_path, {f"{key}_seg{number}": seg})

                print(f"Saved: {save_file_path}")
        else:
            raise KeyError(f"'{key}' key not found in {file_path}")