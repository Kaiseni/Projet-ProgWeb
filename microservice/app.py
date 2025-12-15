from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    # Ce message s'affichera sur votre navigateur
    return "Bravo ! Le microservice est en ligne (Version 1.0)"

@app.route('/health')
def health():
    # Une route utile pour que Kubernetes vérifie si l'app va bien
    return "OK", 200

if __name__ == "__main__":
    # IMPORTANT : host='0.0.0.0' est obligatoire pour Docker
    # Cela permet au conteneur d'être accessible de l'extérieur
    app.run(host='0.0.0.0', port=5000)