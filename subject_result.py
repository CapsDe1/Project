import numpy as np

RATIO = 0.1

def subject_and_data(y, sbj, num, pred):
    sbj_and_data_dic = {}

    for i in range(len(sbj)):
        subject = sbj[i]
        number = num[i]
        prediction = pred[i]
        label = y[i]

        if subject not in sbj_and_data_dic:
            sbj_and_data_dic[subject] = {"seg": [], "pred": [], "y": []}

        sbj_and_data_dic[subject]["seg"].append(number)
        sbj_and_data_dic[subject]["pred"].append(prediction.item())
        sbj_and_data_dic[subject]["y"].append(label)
    
    return sbj_and_data_dic

def suject_y_and_pred(sbj_and_data_dic):
    y_true = []
    y_pred = []
    y_ratio = []

    for _, data in sbj_and_data_dic.items():
        num_correct = []
        num_incorrect = []
        num_seg = len(data["seg"])
        y = data["y"][0] if all(item == data["y"][0] for item in data["y"]) else None
        y_true.append(y)

        predictions = data["pred"]  # 리스트로 추출
        binary_pred = [1 if value >= 0.5 else 0 for value in predictions]  # 0과 1로 변환

        # True와 False의 비율 계산
        true_count = sum(binary_pred)  # True(1)의 개수
        false_count = len(binary_pred) - true_count  # False(0)의 개수
        true_ratio = true_count / len(binary_pred) if len(binary_pred) > 0 else 0

        # 새로운 변수 할당
        if true_ratio >= 0.75:
            assigned = 1  # True 비율이 높으면 2
        elif true_ratio == -1:
            assigned = 2  # True 비율이 낮으면 0
        else:
            assigned = 0  # 그 외에는 1
        
        y_pred.append(assigned)

        # 0 또는 1의 비율 계산
        result = -1
        if y == 0:
            result = binary_pred.count(0) / len(binary_pred)
        elif y == 1:
            result = binary_pred.count(1) / len(binary_pred)
        y_ratio.append(result)

    return y_true, y_pred, y_ratio