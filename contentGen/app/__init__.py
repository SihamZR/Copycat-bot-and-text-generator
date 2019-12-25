import os

from flask import Flask,render_template,request
from flask_bootstrap import Bootstrap
import app.controllers.controllerManager as cm

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        #DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )
    Bootstrap(app)
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    #Routes    
    #------

    #Index 
    @app.route('/')
    def index():
        return render_template("index.html")

    @app.route('/generate', methods=['POST'])
    def generate():
        clicked=None
        if request.method == "POST":
            summary=request.form.get('summary')
            return cm.textGen(summary)
        return 'error : not POST'

    return app