__author__ = 'camden'


from flask import render_template, request, Response, Flask, jsonify
import os
import geocoding as gc
from geojson import dumps, loads

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)

@app.route('/')
def index():
    try:
        with open('static/features.json', 'r') as gj:
            geoj = loads(gj.read())
        return render_template('index.html', geoj = geoj)
    except IOError:
        return render_template('index.html', geoj = 0)
@app.route('/feature', methods=['GET'])
def feature():
    lat = request.args.get('lat', 1, type=float)
    lng = request.args.get('lng', 1, type=float)
    name = request.args.get('name', 1, type=str)
    addr = request.args.get('addr', 1, type=str)
    loc = request.args.get('loc', 1, type=str)
    f = gc.create_feature(lat, lng, name, addr, loc)
    resp = gc.create_geojson(f)
    return jsonify(result = f)

if __name__ == "__main__":
    app.run(debug=True)