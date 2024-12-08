import os

import scipy.io as sio

def init(dir_path_load: str, dir_path_save: str):
    os.makedirs(dir_path_save, exist_ok=True)

    for file_name in os.listdir(dir_path_load):
        if not file_name.endswith('.mat'):
            print(f"'{file_name}' doesn't end with '.mat'")
            continue
            
        # get subject
        sbj = os.path.splitext(file_name)[0]

        # load data
        file_path_load = os.path.join(dir_path_load, file_name)
        mat_dictionary = sio.loadmat(file_path_load)
        x = mat_dictionary[sbj]

        # make key(= sbj_num)
        key = sbj + "_0"
        # save mat
        file_path_save = os.path.join(dir_path_save, f"{key}.mat")
        sio.savemat(file_path_save, {key: x})