#import model
import app.AI.copyCat.CopyCat as cc
import json
def generateTweet(seed,style):
    #feed the input to the model we imported
    #get the output samples
    #return the samples as a json file or ...etc
    #samples = ['this is the first phrase','this is the second phrase','this is the third phrase']
    samples = cc.getSamples(seed,style)
    samplesJson = json.dumps(samples)
    return samplesJson