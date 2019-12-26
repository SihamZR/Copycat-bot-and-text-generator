import interactive_conditional_samples as ics
import json

summary = 'this is a random phrase that will be used as a prompt for the model to use, in hope for it to generate more content that has both substance and fluff'
smpls = ics.interact_model(summary)

samplesJson = json.dumps(smpls)
file = open('sample.txt','w')
file.write(samplesJson)
file.close()