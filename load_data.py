import os
import numpy as np
import scipy.io as sio
from typing import Tuple

def load_data(x_path: str, label: int) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    # return values
    x = []
    y = []
    sbj = []
    num = []

    for file_name in sorted(os.listdir(x_path)):
        if not file_name.endswith('.mat'):
            print(f"'{file_name}' is invalid")
            continue

        #get key & subject( from key)
        key = os.path.splitext(file_name)[0]
        sbj.append(key.split("_")[0])
        num.append(key.split("_")[1])

        # get x
        file_path = os.path.join(x_path, file_name)
        mat_dictionary = sio.loadmat(file_path)
        x.append(mat_dictionary[key])

    x = np.array(x)
    y = np.array([label] * len(x))
    sbj = np.array(sbj)
    num = np.array(num)

    print(f"shape of x in {x_path}: {x.shape}")
    print(f"shape of y in {x_path}: {y.shape}")
    print(f"shape of sbj in {x_path}: {sbj.shape}")
    print(f"shape of num in {x_path}: {num.shape}")
    print(f"{x_path} loaded.")

    return x, y, sbj, num