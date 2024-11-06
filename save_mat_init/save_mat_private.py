import os

import numpy as np

import scipy.io as sio

from source.save_meta import save_meta

meta = {
    "segmentation": "x",
    "value": "raw",
    "dimension": ("time", "channel"),
    "key_order": ["f3", "f4", "c3", "c4", "t3", "t4", "cz", "oz"]
}

key_order = meta["key_order"]

def get_channel_values(file_path):
    values = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            value = [float(val) for val in line.split(':')[1].strip().split()]
            values.append(value)
    return values

def assign_channels(channels, values, x_channels):
    if channels == "f3f4":
        x_channels["f3"] = values[0]
        x_channels["f4"] = values[1]
    elif channels == "c3c4":
        x_channels["c3"] = values[0]
        x_channels["c4"] = values[1]
    elif channels == "t3t4":
        x_channels["t3"] = values[0]
        x_channels["t4"] = values[1]
    elif channels == "czoz":
        x_channels["cz"] = values[0]
        x_channels["oz"] = values[1]
    else:
        raise ValueError(f"Invalid channels: {channels}")

def get_save_path(dir_path_save_common, y, key):
    if y == "0":
        return os.path.join(dir_path_save_common, "HC", f'{key}.mat')
    elif y == "1":
        return os.path.join(dir_path_save_common, "SC", f'{key}.mat')
    elif y == "2":
        return os.path.join(dir_path_save_common, "ADHD", f'{key}.mat')
    else:
        raise ValueError(f"Invalid label '{y}'.")

def save_mat_private(dir_path_load: str, dir_path_save_common: str, meta_path_save: str):
    # create directory for y
    dir_path_save_HC = os.path.join(dir_path_save_common, "HC")
    os.makedirs(dir_path_save_HC, exist_ok=True)
    dir_path_save_SC = os.path.join(dir_path_save_common, "SC")
    os.makedirs(dir_path_save_SC, exist_ok=True)
    dir_path_save_ADHD = os.path.join(dir_path_save_common, "ADHD")
    os.makedirs(dir_path_save_ADHD, exist_ok=True)

    # loop for subject directory
    for dir_name_sbj in os.listdir(dir_path_load):
        dir_path_sbj = os.path.join(dir_path_load, dir_name_sbj, '1차')

        if not os.path.isdir(dir_path_sbj):
            print(f"{dir_name_sbj} is not a directory.")
            continue

        # check subject
        if not (len(dir_name_sbj[-7:-1]) == 6 and dir_name_sbj[-7:-1].isdigit()):
            print(f"{dir_name_sbj} is invalid.")
            continue

        # get key
        key = dir_name_sbj[-7:-1] + "_0"

        # initialization
        x_channels = {ch: None for ch in key_order}
        y = None

        # loop for x_channels
        for file_name in os.listdir(dir_path_sbj):
            file_path = os.path.join(dir_path_sbj, file_name)

            # check if file extension is .txt
            if file_name.endswith('.txt'):

                # get label
                if file_name == "label.txt":
                    with open(file_path, 'r') as file:
                        y = file.read(1)
                    continue
                
                # get xs
                x_two = get_channel_values(file_path)

                # get channels
                channels = file_name[0:4]

                # check channels
                if len(channels) != 4:
                    print(f"{channels} is invalid.")
                    continue
                
                # assign x_two to x_channels
                try:
                    assign_channels(channels, x_two, x_channels)
                except ValueError as e:
                    print(e)
                    continue
        
        # checkk x_channels is fullfilled
        if None in x_channels.values():
            print(f"Incomplete data for {key}. Skipping.")
            continue

        # compose x
        x = np.column_stack([x_channels[key] for key in key_order])

        # save x
        try:
            save_path = get_save_path(dir_path_save_common, y, key)
            sio.savemat(save_path, {key: x})
            print(f"'{save_path}' saved.")
        except ValueError as e:
            print(e)

    # save meta
    save_meta(meta_path_save, meta)
