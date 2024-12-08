from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import numpy as np
import matplotlib.pyplot as plt

def plot_confusion_matrix(y_true, y_pred, label_names):
    # Confusion matrix 계산
    cm = confusion_matrix(y_true, y_pred, labels=[0, 1, 2])
    cm_normalized = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]  # 정규화

    # Confusion matrix display
    fig, ax = plt.subplots(figsize=(8, 6))
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["HC", "ADHD", "SC"])
    disp.plot(cmap=plt.cm.Blues, ax=ax, colorbar=True)

    # 기본 텍스트 제거
    for txt in ax.texts:
        txt.set_visible(False)

    
    # 각 칸에 원래 값과 정규화된 값 추가
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            ax.text(
                j, i, 
                f"{cm[i, j]}\n({cm_normalized[i, j]:.2f})",
                ha="center", va="center", color="black"
            )
    
    plt.title("Confusion Matrix")
    plt.xlabel("Predicted label")
    plt.ylabel("True label")
    plt.show()