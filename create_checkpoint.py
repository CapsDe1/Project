from keras import callbacks

def create_checkpoint(filepath, monitor, mode):
    return callbacks.ModelCheckpoint(
        filepath=filepath,
        monitor=monitor,
        save_best_only=True,
        save_weights_only=False,
        mode=mode
    )