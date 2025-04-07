from flask import Flask
from flask import render_template
from flask import json                                                                                                                                     
app = Flask(__name__)

@app.route('/<int:valeur>')
def exercice(valeur):
a = 0
    count = [str(a)]

    if valeur > 1:
        count.append(str(1))

    for _ in range(2, valeur):
        a = int(count[-1]) + int(count[-2])
        count.append(str(a))

    return ', '.join(count)


if __name__ == "__main__":
    app.run(debug=True)
