import os

import numpy as np

import scipy.io as sio

from source.save_meta import save_meta

meta = {
    "segmentation": "o",
    "dimension": ("time", "channel")
}

def save_mat_segmentation(dir_path_load: str, dir_path_save: str, meta_path_save: str, fs: int, seg_second: int, discarded_second: int):
    # constants
    samples_num_per_seg = seg_second * fs
    discarded_samples_num = discarded_second * fs

    # setting directory for saving
    os.makedirs(dir_path_save, exist_ok=True)

    # loop for unsegmented x
    for file_name in os.listdir(dir_path_load):
        if not file_name.endswith('.mat'):
            raise KeyError(f"'{file_name}' doesn't end with .mat")

        file_path = os.path.join(dir_path_load, file_name)
        mat_dictionary = sio.loadmat(file_path)

        # get key
        key = os.path.splitext(file_name)[0] 

        # get x
        x = mat_dictionary[key]

        # discard discarded_samples_num of x
        x = x[discarded_samples_num:, :]

        # convert type of x to float64
        x = x.astype(np.float64)
    
        samples_num_per_channel = x.shape[0]

        # get segment number
        seg_num = samples_num_per_channel // samples_num_per_seg
        
        # get x discarded the rest of the data at the end
        x = x[:seg_num * samples_num_per_seg, :]

        # segment x
        segs = np.array_split(x, seg_num)

        # get sbj
        sbj = key.split('_')[0]

        # save segmented x
        for num, seg in enumerate(segs, start = 1):
            file_path_save = os.path.join(dir_path_save, f"{sbj}_{num}.mat")
            sio.savemat(file_path_save, {f"{sbj}_{num}": seg})
        
        # print save mat notification
        print(f"'{file_path_save}' saved.")

    # compose meta
    meta["from"] = dir_path_load
    meta["seg_second"] = seg_second
    meta["discarded_second"] = discarded_second

    # save meta
    save_meta(meta_path_save, meta)