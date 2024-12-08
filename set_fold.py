import os
import numpy as np
import scipy.io as sio
import shutil
from typing import List, Tuple

def set_fold(x_path_and_y: List[Tuple[str, str]], fold_i_path: str, k_fold: int,
             fold_i_test_subject_path: str):
    
    # setting directories
    for fold_index, purpose in fold_i_path.items():
        for purpose_index, label in purpose.items():
            for label_index, path in label.items():
                os.makedirs(path, exist_ok=True)

    # set fold
    for x_path, y in x_path_and_y:
        for file_name in sorted(os.listdir(x_path)):
            if not file_name.endswith('.mat'):
                print(f"'{file_name}' is invalid")
                continue
            
            #get key & subject( from key)
            key = os.path.splitext(file_name)[0]
            sbj = key.split("_")[0]

            file_path = os.path.join(x_path, file_name)

            for i in range(k_fold):
                if (sbj in fold_i_test_subject_path[i]):
                    test_file_path = os.path.join(fold_i_path[i]["test"][y], file_name)
                    shutil.copy(file_path, test_file_path)
                elif not (sbj in fold_i_test_subject_path[i]):
                    train_file_path = os.path.join(fold_i_path[i]["train"][y], file_name)
                    shutil.copy(file_path, train_file_path)
                else:
                    print(f"something is invalid")

"""

def set_fold(x_path_and_y: List[Tuple[str, str]], fold_i_path: str, k_fold: int,
             fold_i_test_subject_path: str):
    
    # setting directories
    for fold_index, purpose in fold_i_path.items():
        for purpose_index, label in purpose.items():
            for label_index, path in label.items():
                os.makedirs(path, exist_ok=True)

    # set fold
    for x_path, y in x_path_and_y:
        for file_name in sorted(os.listdir(x_path)):
            if not file_name.endswith('.mat'):
                print(f"'{file_name}' is invalid")
                continue
            
            #get key & subject( from key)
            key = os.path.splitext(file_name)[0]
            sbj = key.split("_")[0]

            file_path = os.path.join(x_path, file_name)

            for i in range(k_fold):
                if (sbj in fold_i_test_subject_path[i]):
                    test_file_path = os.path.join(fold_i_path[i]["test"][y], file_name)
                    shutil.copy(file_path, test_file_path)
                elif (sbj in fold_i_test_subject_path[(i + 1)%k_fold]):
                    train_file_path = os.path.join(fold_i_path[i]["validation"][y], file_name)
                    shutil.copy(file_path, train_file_path)
                elif (not sbj in fold_i_test_subject_path[i]) and (not sbj in fold_i_test_subject_path[(i + 1)%k_fold]):
                    train_file_path = os.path.join(fold_i_path[i]["train"][y], file_name)
                    shutil.copy(file_path, train_file_path)
                else:
                    print(f"something is invalid")

def get_data(dir_path_load: str, label: int):
    x = []
    y = []
    sbj = []

    for file_name in sorted(os.listdir(dir_path_load)):
        if not file_name.endswith('.mat'):
            print(f"'{file_name}' is invalid")
            continue

        #get key & subject( from key)
        key = os.path.splitext(file_name)[0]
        x.append(key)
        sbj.append(key.split("_")[0])

    x = np.array(x)
    y = np.array([label] * len(x))
    sbj = np.array(sbj)

    return x, y, sbj

def set_fold1(x_path_and_y: List[Tuple[str, int]], fold_i_path: str, k_fold: int):
    for fold_index, categories in fold_i_path.items():
        for category, subcategories in categories.items():
            for subcategory, path in subcategories.items():
                os.makedirs(path, exist_ok=True)

    # initialization
    x = None
    y = None
    sbj = None

    x_hc = None
    y_hc = None
    sbj_hc = None
        
    x_adhd = None
    y_adhd = None
    sbj_adhd = None

    # load mat data
    for x_path_arg, y_arg in x_path_and_y:
        x_tmp, y_tmp, sbj_tmp = get_data(x_path_arg, y_arg)
        if y_arg == 0:
            x_hc, y_hc, sbj_hc = x_tmp, y_tmp, sbj_tmp
        elif y_arg == 1:
            x_adhd, y_adhd, sbj_adhd = x_tmp, y_tmp, sbj_tmp
        else:
            print(f"{y_arg} is invalid.")

    x = np.concatenate((x_hc, x_adhd), axis = 0)
    y = np.concatenate((y_hc, y_adhd), axis = 0)
    sbj = np.concatenate((sbj_hc, sbj_adhd), axis = 0)

    sgkf = StratifiedGroupKFold(n_splits=k_fold, random_state=42, shuffle=True)
    folds = list(sgkf.split(x, y, sbj))

    for i in range(k_fold):
        test_index = folds[i][1]
        test_x = x[test_index]
        
        validation_index = folds[(i + 1) % k_fold][1]
        validation_x = x[validation_index]

        train_index = np.setdiff1d(
            np.arange(len(x)), np.concatenate([test_index, validation_index])
        )
        train_x = x[train_index]

        for x_path_arg, y_arg in x_path_and_y:

            if y_arg == 0:
                y_arg = "HC"
            elif y_arg == 1:
                y_arg = "ADHD"
            else:
                print(f"'{y_arg}' is invalid")

            for file_name in sorted(os.listdir(x_path_arg)):
                if not file_name.endswith('.mat'):
                    print(f"'{file_name}' is invalid")
                    continue

                #get key & file_path
                key = os.path.splitext(file_name)[0]
                file_path = os.path.join(x_path_arg, file_name)

                if (key in test_x):
                    test_file_path = os.path.join(fold_i_path[i]["test"][y_arg], file_name)
                    shutil.copy(file_path, test_file_path)
                elif (key in validation_x):
                    validation_file_path = os.path.join(fold_i_path[i]["validation"][y_arg], file_name)
                    shutil.copy(file_path, validation_file_path)
                elif (key in train_x):
                    train_file_path = os.path.join(fold_i_path[i]["train"][y_arg], file_name)
                    shutil.copy(file_path, train_file_path)
                else:
                    print(f"'{key}' is invalid")
                
def set_fold0(dir_path_load: str, label: str, fold_i_path: str, k_fold: int):
    x, y, sbj = get_data(dir_path_load, label)

    sgkf = StratifiedGroupKFold(n_splits=k_fold, random_state=42, shuffle=True)
    folds = list(sgkf.split(x, y, sbj))

    for i in range(k_fold):
        fold_i_test_path = fold_i_path[i]["test"][label]
        os.makedirs(fold_i_test_path, exist_ok=True)
        test_index = folds[i][1]
        test_x = x[test_index]
        
        fold_i_validation_path = fold_i_path[i]["validation"][label]
        os.makedirs(fold_i_validation_path, exist_ok=True)
        validation_index = folds[(i + 1) % k_fold][1]
        validation_x = x[validation_index]

        fold_i_train_path = fold_i_path[i]["train"][label]
        os.makedirs(fold_i_train_path, exist_ok=True)
        train_index = np.setdiff1d(
            np.arange(len(x)), np.concatenate([test_index, validation_index])
        )
        train_x = x[train_index]

        for file_name in sorted(os.listdir(dir_path_load)):
            if not file_name.endswith('.mat'):
                print(f"'{file_name}' is invalid")
                continue

            #get key & file_path
            key = os.path.splitext(file_name)[0]
            file_path = os.path.join(dir_path_load, file_name)

            if (key in test_x):
                test_file_path = os.path.join(fold_i_test_path, file_name)
                shutil.copy(file_path, test_file_path)
            elif (key in validation_x):
                validation_file_path = os.path.join(fold_i_validation_path, file_name)
                shutil.copy(file_path, validation_file_path)
            elif (key in train_x):
                train_file_path = os.path.join(fold_i_train_path, file_name)
                shutil.copy(file_path, train_file_path)
            else:
                print(f"'{key}' is invalid")
"""