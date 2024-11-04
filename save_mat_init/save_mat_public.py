import os

import scipy.io as sio

from source.save_meta import save_meta

meta = {
    "segmentation": "x",
    "value": "raw",
    "dimension": ("time", "channel")
}

def save_mat_public(dir_path_load: str, dir_path_save: str, meta_path_save: str): 
    for file_name in os.listdir(dir_path_load):
        if not file_name.endswith('.mat'):
            print(f"'{file_name}' doesn't end with '.mat'")
            continue
            
        #get subject
        sbj = os.path.splitext(file_name)[0]

        #get key(sbj_num)
        key = sbj + "_0"

        # load data
        file_path_load = os.path.join(dir_path_load, file_name)
        mat_dictionary = sio.loadmat(file_path_load)
        x = mat_dictionary[sbj]

        # save mat
        file_path_save = os.path.join(dir_path_save, f"{key}.mat")
        sio.savemat(file_path_save, {key: x})

        # print save notification
        print(f"'{file_path_save}' saved.")

    save_meta(meta_path_save, meta)