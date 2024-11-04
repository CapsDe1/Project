import numpy as np

import scipy.io as sio

def save_history(history, HISTORY_PATH_SAVE):
    history_data = {key: np.array(value) for key, value in history.history.items()}
    sio.savemat(HISTORY_PATH_SAVE, history_data)
    print(f"{HISTORY_PATH_SAVE} saved.")