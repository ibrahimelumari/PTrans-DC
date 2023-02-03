"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask, jsonify
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import random as rd
from math import sin,cos,sqrt,tan


app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app

@app.route('/matrix_2D')
def generate_2D():
    matrix = np.fromfunction(lambda i,j: i+j, (4,4),dtype=int)
    return jsonify(matrix.tolist())

@app.route('/matrix_3D')
def generate_3D():
    matrix = np.fromfunction(lambda i,j,k : i+j+k, (4,4,4), dtype=int)
    return jsonify(matrix.tolist())

@app.route("/heatmap_data_2d", methods=["GET"])
def heatmap_data_2d():
    n = 200
    data = np.fromfunction(lambda i, j: i + j, (n, n),dtype=int).tolist()
    response = jsonify(data)
    response.headers.add("Access-Control-Allow-Origin", "http://localhost:3000") # allow requests from localhost:3000
    response.headers.add("Access-Control-Allow-Headers", "Content-Type,Authorization")
    response.headers.add("Access-Control-Allow-Methods", "GET,PUT,POST,DELETE,OPTIONS")
    return response

@app.route("/heatmap_data_3d", methods=["GET"])
def heatmap_data_3d():
    n = 200
    data = np.fromfunction(lambda i, j, k: i + j + k, (n, n, n),dtype=int).tolist()
    response = jsonify(data)
    response.headers.add("Access-Control-Allow-Origin", "http://localhost:3000") # allow requests from localhost:3000
    response.headers.add("Access-Control-Allow-Headers", "Content-Type,Authorization")
    response.headers.add("Access-Control-Allow-Methods", "GET,PUT,POST,DELETE,OPTIONS")
    return response

@app.route("/heatmap_random_2d", methods=["GET"])
def heatmap_random_2d():
    n = 100
    vfunc = np.vectorize(lambda x: sin(x))
    data = (np.fromfunction(lambda i, j: (rd.choice([vfunc(i*j),(vfunc(i*j)),((i-j)**3),(j**2)*i,(i+j)**(1/2), (i**2/(j+1))-j ])), (n, n),dtype=int)).tolist()
    response = jsonify(data)
    response.headers.add("Access-Control-Allow-Origin", "http://localhost:3000") # allow requests from localhost:3000
    response.headers.add("Access-Control-Allow-Headers", "Content-Type,Authorization")
    response.headers.add("Access-Control-Allow-Methods", "GET,PUT,POST,DELETE,OPTIONS")
    return response

@app.route('/heatmap_python')
def generate_python_heatmap():
    fig = px.imshow(np.fromfunction(lambda i,j: i+j, (200,200),dtype=int))
    fig.show()
    return fig.show()

@app.route('/')
def hello():
    """Renders a sample page."""
    return "Hello World!"

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
