from flask import Flask, jsonify

app = Flask(__name__)
def matrix_2d(n:int):
    ##rows, cols = (n, m)
    m = [[0]*n]*n
    return m
def matrix_2d_f(n:int, func):
    m = matrix_2d(n)
    for i in range(n):
        for j in range(n):
            m[i][j]=func(i,j)
            print(m)
    return m
def adder(x,y): 
    return x+y
""" def generate_matrix_data():
  x = [1, 2, 3, 4]
  y = [5, 6, 7, 8]
  z = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
  return {'x': x, 'y': y, 'z': z} """
def generate_matrix_data(num_rows, num_columns, func):
  x = [i for i in range(num_columns)]
  y = [i for i in range(num_rows)]
  z = [[func(i, j) for j in range(num_columns)] for i in range(num_rows)]
  return {'x': x, 'y': y, 'z': z}
  
@app.route('/api/matrix')
def get_matrix():
  #matrix_data = generate_matrix_data()
  matrix_data = generate_matrix_data(5, 5, lambda i, j: i + j)
  return jsonify(matrix_data)

if __name__ == '__main__':
  app.run()


#return{"matrix": [str(matrix_2d(5)),str(matrix_2d_f(4,adder))]}