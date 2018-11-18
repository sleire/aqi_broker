from flask import Flask, jsonify, request, Response
import requests

# api token
with open('token') as t:
    tok = t.readlines()[0]

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/get_aqi/<var>', methods = ['GET', 'POST'])
def get_aqi(var):
    url_1 = 'https://api.waqi.info/feed/'
    url_2 = '/?token='
    #r = requests.get(url_1 + var + url_2 +tok)
    #res = json.dumps(r)
    #resp = Response(res, status=200, mimetype='application/json')
    return url_1 + var + url_2 +tok
    #return resp

if __name__ == '__main__':
    app.run()