__author__ = 'camden'

# A very simple Flask Hello World app for you to get started with...

from flask import render_template, request, Response, Flask, jsonify
import os
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)