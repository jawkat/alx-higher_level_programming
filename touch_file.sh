#!/bin/bash

echo "Enter the filename (without extension):"
read filename

# Ajout de l'extension .py si elle n'est pas déjà fournie
filename="$filename.py"

# Création du fichier avec la première ligne
echo "#!/usr/bin/python3" > "$filename"

# Rendre le fichier exécutable
chmod +x "$filename"

# Afficher un message de confirmation
echo "File $filename created and made executable successfully."
