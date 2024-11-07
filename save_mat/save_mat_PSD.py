import os

import numpy as np

import scipy.io as sio

from scipy.signal import welch

from source.save_meta import save_meta

meta = {
    "value": "PSD",
    "dimension": ("time", "channel")
}

def save_mat_PSD(dir_path_load: str, dir_path_save: str, meta_path_save: str, fs: int):
    # setting directory for saving
    os.makedirs(dir_path_save, exist_ok=True)

    for file_name in os.listdir(dir_path_load):
        if not file_name.endswith('.mat'):
            raise KeyError(f"'{file_name}' doesn't end with .mat")
        
        file_path = os.path.join(dir_path_load, file_name)
        mat_dictionary = sio.loadmat(file_path)
        
        # get key
        key = os.path.splitext(file_name)[0]

        # get x
        x = mat_dictionary[key]

        channel_number = x.shape[1]

        # initialization
        psd = []

        # get psd of channels
        for channel in range(channel_number):
            x_channel = x[:, channel]
            _, psd_channel = welch(x_channel, fs=fs, nperseg=fs)
            psd.append(psd_channel)
        
        psd = np.array(psd).T

        file_path_save = os.path.join(dir_path_save, f"{key}.mat")
        sio.savemat(file_path_save, {f"{key}": psd})
        print(f"'{file_path_save}' saved.")

    # compose meta
    meta["from"] = dir_path_load

    # save meta
    save_meta(meta_path_save, meta)