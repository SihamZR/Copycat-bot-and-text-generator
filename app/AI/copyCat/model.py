from keras.models import Sequential
from keras.layers import LSTM, Dense, Activation

def genModel(layerCount,hiddenLayerDim,vocabSize):
    model = Sequential()
    for i in range(layerCount):
        if (i!=(layerCount-1)):
            return_seq_flg=True
        else:
            return_seq_flg=False
            
        model.add(
                LSTM(
                    hiddenLayerDim, 
                    return_sequences=return_seq_flg,
                    batch_input_shape=(1, 1, vocabSize),
                    stateful=True
                )
            )
    model.add(Dense(vocabSize))
    model.add(Activation('softmax'))
    model.compile(loss='categorical_crossentropy', optimizer="adam")

    return model