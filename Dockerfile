# Utilisez une image officielle Python comme base
FROM python:3.10-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier le fichier requirements.txt et installer les dépendances
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copier tous les fichiers du projet
COPY . /app

# Exposer le port utilisé par Django (par défaut : 8000)
EXPOSE 8000

# Lancer les migrations, collecter les fichiers statiques, et démarrer le serveur
CMD ["sh", "-c", "python manage.py migrate && python manage.py collectstatic --noinput && python manage.py runserver 0.0.0.0:8000"]
