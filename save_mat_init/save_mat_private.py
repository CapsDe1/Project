import os

import numpy as np

import scipy.io as sio

from source.save_meta import save_meta

meta = {
    "segmentation": "x",
    "value": "raw",
    "dimension": ("time", "channel")
}

def private_save_mat(dir_path_load_common: str, dir_path_save_common: str):
    for dir_name_sbj in os.listdir(dir_path_load_common):
        dir_path_sbj = os.path.join(dir_path_load_common, dir_name_sbj)

        if not os.path.isdir(dir_path_sbj):
            print(f"{dir_name_sbj} is not a directory.")
            continue

        dir_path_txt = os.path.join(dir_path_sbj, '1차')

        if not os.path.exists(dir_path_txt):
            print(f"{dir_path_txt} doesn't exist.")
            continue
        
        #initialization
        x = []
        label = None
        channel = {"f3f4": 0, }

        if not (len(dir_name_sbj[-7:-1]) == 6 and dir_name_sbj[-7:-1].isdigit()):
            print(f"{dir_name_sbj} is invalid.")
            continue

        # get key
        key = dir_name_sbj[-7:-1] + "_0"

        for file_name in os.listdir(dir_path_txt):
            file_path = os.path.join(dir_path_txt, file_name)

            if not file_name.endswith('.txt'):
                print(f"{file_path} is not a '.txt' file.")
                continue
            
            # get y
            if file_name == "label.txt":
                with open(file_path, 'r') as file:
                    label = file.read(1)
                continue

            channels = dir_name_sbj[0:4]

            if not len(channels) == 4:
                print(f"{channels} is invalid.")
                continue
            
            # get channel x
            channel_x = []
            # get data
            with open(file_path, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    if not line.startswith("CN"):
                        print(f"A line of {file_path} doesn't start with 'CN'.")
                    channel_x_str = line.split(':')[1].strip().split()
                    channel_x.append([float(x) for data in channel_x_str])

            if channels == "f3f4":
                print()
            elif channels == "c3c4":
                print()
            elif channels == "t3t4":
                print()
            elif channels == "czoz":
                print()
            else:
                print(f"{channels} is invalid.")
                continue
        
        # transpose x
        x = np.array(x).T

        # save mat
        if label == "0":
            print()
        elif label == "1":
            print()
        elif label == "2":
            print()
        else:
            print(f"Invalid label '{label}' for subject '{dir_name_sbj}'.")
        save_mat_path = os.path.join(save_dir_path_dictionary[label], f"{key}{FILE_EXTENSION_MAT}")
        sio.savemat(save_mat_path, {key: x})

        # print save mat notification
        print(f"'{save_mat_path}' saved.")

    save_meta(meta_path_save, meta)