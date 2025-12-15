# 1. On part d'une image Linux légère avec Python déjà installé
FROM python:3.9-slim

# 2. On crée un dossier de travail à l'intérieur du conteneur
WORKDIR /app

# 3. On copie d'abord les dépendances (optimisation du cache Docker)
COPY requirements.txt .

# 4. On installe les librairies listées
RUN pip install --no-cache-dir -r requirements.txt

# 5. On copie tout le reste du code (votre app.py, etc.) dans le conteneur
COPY . .

# 6. On indique sur quel port l'app écoute (ex: 5000 pour Flask, 8000 pour FastAPI)
EXPOSE 5000

# 7. La commande pour démarrer votre application
CMD ["python", "app.py"]