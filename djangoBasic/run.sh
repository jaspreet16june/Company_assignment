#!/bin/bash

# Install requirements
pip install -r requirements.txt

# Apply migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser
echo "from company_app.models import CustomUser; CustomUser.objects.create_superuser('admin@example.com', 'admin')" | python manage.py shell

# Run server
python manage.py runserver
