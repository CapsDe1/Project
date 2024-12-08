import numpy as np
from sklearn.utils import shuffle

from load_data import load_data

def process_data(x_path_and_y, random_state=42):

    x_list, y_list, sbj_list, num_list = [], [], [], []

    for x_path, y in x_path_and_y:
        if y == "HC":
            y = 0
        elif y == "ADHD":
            y = 1
        else:
            print(f"{y} is invalid.")
            
        x, y, sbj, num = load_data(x_path, y)
        x_list.append(x)
        y_list.append(y)
        sbj_list.append(sbj)
        num_list.append(num)

    x_combined = np.concatenate(x_list, axis=0)
    y_combined = np.concatenate(y_list, axis=0)
    sbj_combined = np.concatenate(sbj_list, axis=0)
    num_combined = np.concatenate(num_list, axis=0)

    x_combined, y_combined, sbj_combined, num_combined = shuffle(x_combined, y_combined,
                                                                 sbj_combined, num_combined,
                                                                 random_state=random_state)
    x_combined = np.expand_dims(x_combined, axis=-1)

    return x_combined, y_combined, sbj_combined, num_combined