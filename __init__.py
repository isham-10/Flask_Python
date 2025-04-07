from flask import Flask
from flask import render_template
from flask import json                                                                                                                                     
app = Flask(__name__)                                                                                                                  


@app.route('/')
def index():
    n = request.args.get('n', default=5, type=int)
    result = generate_pyramid(n)
    return f'<pre>{result}</pre>'

def generate_pyramid(n):
    pyramid = ''
    for i in range(1, n + 1):
        pyramid += ' ' * (n - i)
        pyramid += ''.join(str(j) for j in range(1, i + 1))
        pyramid += ''.join(str(j) for j in range(i - 1, 0, -1))
        pyramid += '\n'
    return pyramid

   

if __name__ == "__main__":
  app.run(debug=True)
