from keras import utils
import math

class DataGenerator(utils.Sequence):
    def __init__(self, x_data, y_data=None, batch_size=24):
        self.x_data = x_data
        self.y_data = y_data
        self.batch_size = batch_size
        self.n_batches = math.ceil(len(x_data) / batch_size)

    def __len__(self):
        return self.n_batches

    def __getitem__(self, idx):
        start = idx * self.batch_size
        end = start + self.batch_size
        batch_x = self.x_data[start:end]
        
        # y_data가 있을 경우 y를 반환
        if self.y_data is not None:
            batch_y = self.y_data[start:end]
            return batch_x, batch_y
        else:
            # y_data가 없으면 x만 반환
            return batch_x
