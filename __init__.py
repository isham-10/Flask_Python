from flask import Flask
from flask import render_template
from flask import json                                                                                                                                     
app = Flask(__name__)                                                                                                                  


@app.route('/<int:valeur>')
def exercice(valeur):
    etoiles = ''
    for i in range(valeur):
        etoiles += '*'
    return etoiles #comm 
def generate_pattern(valeur):
    for i in range(valeur):
        print('*' * valeur)



if __name__ == "__main__":
  app.run(debug=True)
