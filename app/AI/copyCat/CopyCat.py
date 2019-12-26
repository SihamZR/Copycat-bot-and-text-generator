import sys
import numpy as np
import string
from keras.models import Sequential
from keras.layers import LSTM, Dense, Activation
import os
import app.AI.copyCat.model as copyCat
LAYER_COUNT = 4
HIDDEN_LAYERS_DIM = 512
# generic vocabulary， copied from TRAINING
characters = [' ', '!', '"', '#', '$', '%', '&', "'", ',', '.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '_', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

VOCABULARY_SIZE = len(characters)
characters_to_ix = {c:i for i,c in enumerate(characters)}





def sample(preds, temperature=1.0):
    # Helper function to sample an index from a probability array
    # from fchollet/keras
    preds = np.asarray(preds).astype('float64')
    preds = np.log(preds) / temperature
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)
    probas = np.random.multinomial(1, preds, 1)
    return np.argmax(probas)

def predict_next_char(model, current_char, diversity=1.0):
    # Predict the next character from the current one
    x = np.zeros((1, 1, VOCABULARY_SIZE))
    x[:,:,characters_to_ix[current_char]] = 1
    y = model.predict(x, batch_size=1)
    next_char_ix = sample(y[0,:], temperature=diversity)
    next_char = characters[next_char_ix]
    return next_char

def generate_text(model, seed="I am", count=140):
    # Generate characters from a given seed
    outputText =""
    model.reset_states()
    for s in seed[:-1]:
        next_char = predict_next_char(model, s)
    current_char = seed[-1]

    outputText+="["+seed+"]"
    
    for i in range(count - len(seed)):
        next_char = predict_next_char(model, current_char, diversity=0.5)
        current_char = next_char
        outputText+=next_char
    return outputText

def getSamples(seed,style,samples=5):

    currentPath=os.path.dirname(os.path.dirname(__file__))
    if style=="Trump":
        filepath = os.path.join(currentPath,"models/Trump.1827_weights")
    else:
        filepath = os.path.join(currentPath,"models/Obama.0280_weights")
    test_model = copyCat.genModel(LAYER_COUNT,HIDDEN_LAYERS_DIM,VOCABULARY_SIZE)
    test_model.load_weights(
        filepath
    )
    outputArr = []
    for i in range(samples):
        outputArr.append(generate_text(
            test_model,
            seed=seed
        ))
    return outputArr