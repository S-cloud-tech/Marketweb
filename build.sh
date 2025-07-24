#!/bin/sh

echo "Creating a virtual environment..."
python3 -m venv env
source venv/bin/activate

echo "Upgrading pip..."
pip install --upgrade pip

echo "Installing latest versions of listed packages..."
pip install --upgrade $(cut -d= -f1 requirements.txt)

echo "Freezing new versions into requirements.txt..."
pip freeze > requirements.txt

deactivate
rm -rf env

echo "requirements.txt updated with latest package versions."

echo "Running migrations..."
python manage.py migrate

echo "Starting server..."
python manage.py runserver 0.0.0.0:8000
