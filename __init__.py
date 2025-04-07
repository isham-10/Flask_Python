from flask import Flask
from flask import render_template
from flask import json                                                                                                                                     
app = Flask(__name__)                                                                                                                  

@app.route('/<int:valeur>')
def fibonacci_sequence(n):
    # Initialiser les deux premiers termes de la suite de Fibonacci
    a, b = 0, 1
    sequence = [a, b]
    
    # Générer la suite de Fibonacci jusqu'au nième terme
    for _ in range(2, n):
        a, b = b, a + b
        sequence.append(b)
    
    return sequence

# Définir la valeur de n
n = 7

# Générer et afficher la suite de Fibonacci jusqu'au nième terme
print(fibonacci_sequence(n))


if __name__ == "__main__":
    app.run(debug=True)
