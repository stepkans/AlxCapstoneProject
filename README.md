# Iloomon Olosho Le Maa | ALX Capstone Project

This is a Capstone project for ALX AFRICA's Software Engineering:
In this project I did BloggingAPI using Django and Django Rest Framework.
Iloomon Olosho Le Maa (News around Maasai Speakers) is a news blog in Maa Speaking 
Communities.

### Application Setup

You should have at least basic django and django-rest framework experience to run this api. 
We tested this using only in PostgreSQL and Sqlite databases.

### Clone the repo
Clone the  repo

`git clone https://github.com/stepkans/AlxCapstoneProject.git`  

### Create a virtual environment

There are several ways depending on the OS and package you choose. Here's my favorite  
`sudo apt-get install python3-pip`  
`pip3 install virtualenv`  
Then either  
`python3 -m venv venv`  
or  
`python -m venv venv`  
or  
`virtualenv venv` (you can call it venv or anything you like)

#### Activate the virtual environment  

in Mac or Linux
`source venv/bin/activate`  
in windows
`venv/Scripts/activate.bat`  

### Running the project
```python
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

#### Deployment 
This app is deployed at [pythonanywhere](https://iloomonlemaa.pythonanywhere.com/)
