from flask import Flask
from flask import render_template
from flask import json                                                                                                                                     
app = Flask(__name__)

app = Flask(_name_)

@app.route('/<int:n>')
def exercice(n):
    seq = ['0', '1'] if n > 1 else ['0']

    for _ in range(2, n):
        seq.append(str(int(seq[-1]) + int(seq[-2])))

    return ', '.join(seq[:n])
app = Flask(_name_)

@app.route('/<int:n>')
def exercice(n):
    seq = ['0', '1'] if n > 1 else ['0']

    for _ in range(2, n):
        seq.append(str(int(seq[-1]) + int(seq[-2])))

    return ', '.join(seq[:n])




if __name__ == "__main__":
    app.run(debug=True)
