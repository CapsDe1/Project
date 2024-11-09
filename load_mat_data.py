import os

import numpy as np

import scipy.io as sio

from typing import Tuple

def load_mat_data(dir_path: str, label: int) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    # return values
    x = []
    y = []
    sbj = []
    num = []

    #loop for file_names in dir_path
    for file_name in os.listdir(dir_path):
        if file_name.endswith('.mat'):
            #get key
            key = os.path.splitext(file_name)[0]

            #get sbj & num( from key)
            sbj.append(key.split("_")[0])
            num.append(key.split("_")[1])

            #load mat dictionary
            file_path = os.path.join(dir_path, file_name)
            mat_dictionary = sio.loadmat(file_path)

            #append to x
            x.append(mat_dictionary[key])
        else:
            print(f"'{file_name}' doesn't end with '{'.mat'}'")

    x = np.array(x)
    y = np.array([label] * len(x))
    sbj = np.array(sbj)
    num = np.array(num)

    print(f"shape of x in {dir_path}: {x.shape}")
    print(f"shape of y in {dir_path}: {y.shape}")
    print(f"shape of sbj in {dir_path}: {sbj.shape}")
    print(f"shape of num in {dir_path}: {num.shape}")

    return x, y, sbj, num