run:
	python manage.py runserver

server:
	python manage.py makemigrations
	python manage.py migrate
	python manage.py runserver

admin:
	python manage.py createsuperuser	


