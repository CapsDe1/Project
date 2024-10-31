import os

import numpy as np

import scipy.io as sio

from scipy.signal import welch

def save_PSD_mat(dir_path, save_dir_path, fs):
    os.makedirs(os.path.join(save_dir_path), exist_ok=True)

    for file_name in os.listdir(dir_path):
        if file_name.endswith('.mat'):
            file_path = os.path.join(dir_path, file_name)
            key = os.path.splitext(file_name)[0]
            mat_data = sio.loadmat(file_path)
            
            data = mat_data[key]
            psd = []
            f = []
            channel_num = data.shape[1]
            for channel in range(channel_num):
                channel_data = data[:, channel]
                f, channel_psd = welch(channel_data, fs=fs, nperseg=fs)
                psd.append(channel_psd)
            
            psd = np.array(psd)
            f = np.array(f)
            psd_fs = fs // 2
            if psd.shape[1] >= psd_fs:
                psd = psd[:, :psd_fs].T
                save_file_path = os.path.join(save_dir_path, f"{key}.mat")
                sio.savemat(save_file_path, {f'{key}': psd, 'f': f})
            else:
                raise ValueError(f"PSD data is too small for {key}. Expected at least {psd_fs} frequency bins.")
        else:
            raise KeyError(f"'{key}' key not found in {file_path}")