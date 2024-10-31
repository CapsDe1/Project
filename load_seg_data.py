import os

import numpy as np

import scipy.io as sio

def load_seg_data(dir_path: str, label: int):
    x = []
    y = []
    sbj = []
    seg = []

    for file_name in os.listdir(dir_path):
        if file_name.endswith('.mat'):
            key = os.path.splitext(file_name)[0]
            file_path = os.path.join(dir_path, file_name)
            mat_data = sio.loadmat(file_path)

            data = mat_data[key]
            x.append(data)
            y.append(label)
            sbj.append(key.split("_")[0])
            seg.append(key.split("_")[1])
            
    return np.array(x), np.array(y), np.array(sbj), np.array(seg)