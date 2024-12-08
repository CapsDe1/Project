import numpy as np

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

def evaluate_predictions_train(y_true, y_pred):
    return accuracy_score(y_true, y_pred)

def evaluate_predictions_test(y_true, y_pred):
    return {
        "accuracy": accuracy_score(y_true, y_pred),
        "precision_adhd": precision_score(y_true, y_pred, pos_label=1),
        "precision_control": precision_score(y_true, y_pred, pos_label=0),
        "recall_adhd": recall_score(y_true, y_pred, pos_label=1),
        "recall_control": recall_score(y_true, y_pred, pos_label=0),
        "f1_adhd": f1_score(y_true, y_pred, pos_label=1),
        "f1_control": f1_score(y_true, y_pred, pos_label=0),
        "auc": roc_auc_score(y_true, y_pred),
    }