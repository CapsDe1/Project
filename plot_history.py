import os

import scipy.io as sio

import matplotlib.pyplot as plt

def plot_history(dir_path_load: str):
    for file_name in os.listdir(dir_path_load):
        if not file_name.endswith('.mat'):
            print(f"{file_name} is invalid.")

        file_path = os.path.join(dir_path_load, file_name)
        history_dictionary = sio.loadmat(file_path)
    
        metrics = list(history_dictionary.keys())
        print(metrics)
        for metric in metrics:
            if 'val_' + metric in metrics:
                print(metric)
                plt.figure(figsize=(10, 6))
                print(history_dictionary[metric])
                plt.plot(history_dictionary[metric].squeeze(), label=f'Train {metric}')
                plt.plot(history_dictionary['val_' + metric].squeeze(), label=f'Validation {metric}')
                
                plt.title(f'Train vs Validation {metric} {file_name}')
                plt.xlabel('Epochs')
                plt.ylabel(metric)
                plt.xlim(0, 100)
                if metric == 'loss':
                    plt.ylim(0, 5)
                else:
                    plt.ylim(0, 1)
                plt.legend()
                plt.grid(True)
                plt.show()