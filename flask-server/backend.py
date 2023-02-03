from flask import Flask, jsonify
import numpy as np

app = Flask(__name__)

def generate_matrix_data():
  x = [1, 2, 3, 4]
  y = [5, 6, 7, 8]
  z = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
  return {'x': x, 'y': y, 'z': z}

def generate_2D_matrix():
	matrix = np.fromfunction(lambda i, j: i + j, (4, 4), dtype=int)
	return matrix.tolist()

@app.route('/api/matrix')
def get_matrix():
  matrix_data = generate_matrix_data()
  return jsonify(matrix_data)

@app.route('/api/matrix')
def get_matrix_2D():
	m2D = generate_2D_matrix()
	return jsonify(m2D)
if __name__ == '__main__':
  app.run()