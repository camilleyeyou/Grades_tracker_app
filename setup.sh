#!/bin/bash

# Check if Python is installed
if ! command -v python3 &> /dev/null
then
    echo "Python 3 is not installed. Please install Python 3 and try again."
    exit 1
fi

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install dependencies
pip install django gunicorn whitenoise dj-database-url

# Run migrations
python3 manage.py migrate

# Create a superuser (optional)
read -p "Do you want to create a superuser? (y/n): " create_superuser
if [ "$create_superuser" == "y" ]; then
    python3 manage.py createsuperuser
fi

# Start the development server
echo "Starting the development server..."
python3 manage.py runserver