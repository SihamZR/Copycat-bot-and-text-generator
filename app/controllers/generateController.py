#import model
import app.AI.GenText.getSamples as gs
import json
def generateText(summary):
    #feed the input to the model we imported
    #get the output samples
    #return the samples as a json file or ...etc
    samples = gs.interact_model(str(summary))
    samplesJson = json.dumps(samples)
    return samplesJson