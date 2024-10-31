from keras import models, layers, optimizers, regularizers, metrics

def cnn(shape):
    model = models.Sequential()

    # Input Layer
    model.add(layers.InputLayer(shape=shape, batch_size=32))
    
    # 1st Residual Block
    model.add(layers.Conv2D(64, (3, 3), padding='same', name='conv1'))
    model.add(layers.BatchNormalization(name='batch_norm1'))
    model.add(layers.ReLU(name='relu1'))
    model.add(layers.MaxPooling2D((2, 2), name='maxpool1'))
    model.add(layers.Dropout(0.3, name='dropout1'))

    # 2nd Residual Block
    model.add(layers.Conv2D(128, (3, 3), padding='same', name='conv2'))
    model.add(layers.BatchNormalization(name='batch_norm2'))
    model.add(layers.ReLU(name='relu2'))
    model.add(layers.MaxPooling2D((2, 2), name='maxpool2'))
    model.add(layers.Dropout(0.4, name='dropout2'))

    # 3rd Residual Block
    model.add(layers.Conv2D(256, (3, 3), padding='same', name='conv3'))
    model.add(layers.BatchNormalization(name='batch_norm3'))
    model.add(layers.ReLU(name='relu3'))
    model.add(layers.MaxPooling2D((2, 2), name='maxpool3'))
    model.add(layers.Dropout(0.5, name='dropout3'))

    # 4th Residual Block
    model.add(layers.Conv2D(512, (3, 3), padding='same', name='conv4'))
    model.add(layers.BatchNormalization(name='batch_norm4'))
    model.add(layers.ReLU(name='relu4'))
    model.add(layers.MaxPooling2D((2, 2), name='maxpool4'))
    model.add(layers.Dropout(0.5, name='dropout4'))

    # Fully Connected Layer
    model.add(layers.Flatten(name='flatten'))
    model.add(layers.Dense(256, activation='relu', kernel_regularizer=regularizers.l2(0.001), name='fc1'))
    model.add(layers.Dropout(0.5, name='dropout5'))

    # Output Layer
    model.add(layers.Dense(1, activation='sigmoid', name='output'))

    model.compile(optimizer=optimizers.Adam(learning_rate=0.001), loss='binary_crossentropy', metrics=['accuracy'])

    return model