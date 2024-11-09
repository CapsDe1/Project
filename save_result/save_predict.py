import numpy as np

import scipy.io as sio

#constants
from source.constants import PREDICT

def save_predict(y_prob, y_test, sbj_test, num_test, PREDICT_PATH_SAVE):
    y_prob = np.array(y_prob).T

    y_pred = None
    if y_prob.shape[0] == 1:
        y_pred = (y_prob >= 0.5).astype(int)
    else:
        y_pred = np.argmax(y_prob, axis=0)
    
    key = [f"{s}_{n}" for s, n in zip(sbj_test, num_test)]
    incorrect_indices = np.where(y_pred != y_test)[1]

    predict_data = {
        PREDICT.Y_PROB: y_prob,
        PREDICT.Y_PRED: y_pred,
        PREDICT.Y_TEST: y_test,
        PREDICT.KEY: key,
        PREDICT.INCORRECT_INDICES: incorrect_indices,
    }
    
    sio.savemat(PREDICT_PATH_SAVE, predict_data)
    print(f"{PREDICT_PATH_SAVE} saved.")