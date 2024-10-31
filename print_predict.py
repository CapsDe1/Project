import numpy as np

from codes.print_confusion_matrix import print_confusion_matrix

def print_predict(pred, y_test, sbj_test, seg_test, fold_num):
    pred = pred.flatten()
    
    pred_str = pred.astype(str)

    with open(f"pred_fold_{fold_num}.txt", "w") as file:
        file.write(" ".join(pred_str))

    y_pred = (pred >= 0.5).astype(int)
    incorrect_indices = np.where(y_pred != y_test)[0]
    
    incorrect = [f"{sbj_test[i]}_{seg_test[i]}: {pred[i]}" for i in incorrect_indices]
    with open(f"incorrect_fold_{fold_num}.txt", "w") as file:
        file.write(" ".join(incorrect))

    print_confusion_matrix(y_test, y_pred, ["ADHD", "HC"])
    print(f"----------Incorrect Predictions----------")
    for i in incorrect_indices:
        print(f"Index: {i}, Predicted Label: {pred_str[i]}, True Label: {y_test[i]}, Subject_Segment: {sbj_test[i]}_{seg_test[i]}")