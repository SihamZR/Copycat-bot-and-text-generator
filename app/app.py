import os

from flask import Flask,render_template,request
from flask_bootstrap import Bootstrap
import controllers.controllerManager as cm
app = Flask(__name__)

#Index 
@app.route('/')
def index():
    return render_template("index.html",value='0')
@app.route('/holy')
def holy():
    return render_template("holy.html",value='0')

@app.route('/copycat')
def copycat():
    return render_template("copycat.html",value='1')

@app.route('/generateCC', methods=['POST'])
def generateCC():
    clicked=None
    if request.method == "POST":
        seed=request.form.get('seed')
        style=request.form.get('style')
        return cm.tweetGen(seed,style)
    return 'error : not POST'

@app.route('/contgen')
def contgen():
    return render_template("generate.html",value='2')

@app.route('/generate', methods=['POST'])
def generate():
    clicked=None
    if request.method == "POST":
        summary=request.form.get('summary')
        return cm.textGen(summary)
    return 'error : not POST'
    
if __name__ == "__main__":
    app.run(debug=True)