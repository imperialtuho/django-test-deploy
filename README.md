# First Start

docker-compose up -d --build

# Create SU

docker-compose exec web python manage.py createsuperuser

# Migration

docker-compose exec web python manage.py makemigrations

# Migrate Data

docker-compose exec web python manage.py migrate

# Turn down Server

docker-compose down

# Turn on Server

docker-compose up
