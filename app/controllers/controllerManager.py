import app.controllers.generateController as genereteController
import app.controllers.tweetController as tweetController

def textGen(summary):
    return genereteController.generateText(summary)
def tweetGen(seed,style):
    return tweetController.generateTweet(seed,style)