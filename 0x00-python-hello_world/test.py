
import os

# Accéder à la valeur de la variable d'environnement PYFILE
pyfile = os.environ.get('PYFILE', 'no')
print(f"Le fichier Python à exécuter est : {pyfile}")
