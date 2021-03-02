from flask import Flask
from flask import request
from calculator import start
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def up():
    return "Hello World!"

@app.route('/compute' , methods = ['POST'])
def compute_isochrone():

    try:
        data = request.json
        origin , isochrone = start(data['address'], data['n_angles'] , data['duration']  , data['mode'] , data['traffic'])
        return {'status' : 'success' , 'result' : isochrone , 'origin' : origin}        
    except Exception as e:
        print(e)
        return {'status' : 'error' , 'message' : str(e)}



if __name__ == '__main__':
    app.run()

#if __name__ == '__main__':
#    from waitress import serve
#    serve(app, host="0.0.0.0", port=8080)
