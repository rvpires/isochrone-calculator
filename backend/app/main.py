from flask import Flask
from flask import request
from app.calculator import start
from flask_cors import CORS
import os
from flask import send_from_directory


app = Flask(__name__, static_folder='../client/dist/',    static_url_path='/')
CORS(app)

@app.route('/')
def up():
    return app.send_static_file('index.html')

@app.route('/compute' , methods = ['POST'])
def compute_isochrone():

    try:
        data = request.json
        origin , isochrone = start(data['address'], data['n_angles'] , data['duration']  , data['mode'] , data['traffic'])
        return {'status' : 'success' , 'result' : isochrone , 'origin' : origin}        
    except Exception as e:
        print(e)
        return {'status' : 'error' , 'message' : str(e)}


