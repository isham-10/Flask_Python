from flask import Flask

app = Flask(__name__)

@app.route('/<path:valeurs>')
def exercice(valeurs):
    liste_nombres = valeurs.split('/')
    liste_nombres = [int(n) for n in liste_nombres]
    resultat = 0
    for n in liste_nombres:
        resultat = resultat + n
    return str(resultat)
    liste_nombres = [int(n) for n in liste_nombres]
    max_value = liste_nombres[0]
    for n in liste_nombres:
        if n > max_value:
            max_value = n

    return f"La somme est : {sum(liste_nombres)}, La valeur maximale est : {max_value}"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
