from flask import Flask
from flask import render_template
from flask import json                                                                                                                                     
app = Flask(__name__)

@app.route('/<int:valeur>')
def calculate_sum(n):
    somme = 0

    for i in range(1, n + 1):
        if i % 11 == 0:
            continue
        if i % 5 == 0 or i % 7 == 0:
            somme += i
        if somme => 5000:
            break

    return somme

n = int(input("Entrez la valeur de n : "))

somme_finale = calculate_sum(n)
print(f"La somme finale est : {somme_finale}")



if __name__ == "__main__":
    app.run(debug=True)
