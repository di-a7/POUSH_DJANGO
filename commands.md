
- Virtual environment:
# install virtualenv
pip install virtualenv

# create virtual environment
python -m venv env    or   virtualenv env         # env is the name of virtual environment

# activate virtual environment
env\Scripts\activate
source env/Scripts/activate   or source env/bin/activate[mac,linux]

# install Django
pip install django

# startproject
django-admin startproject project_name .

# start server
python manage.py runserver

# start app
python manage.py startapp app_name

# make migrations file
python manage.py makemigrations

# create table 
python manage.py migrate

# open python shell
python manage.py shell

# CRUD operation
c: create
R: retrieve
U: Update
D: Delete

# get all data
model_name.objects.all()
model_name.objects.all().values()

# data create (Create)
model_name.objects.create(field1 = "...", field2 = "...", field3 = "...", .....)

# single data fetch  (retrieve)
a = model_name.objects.get(id = 1)

# Update existing data  (Update)
a.title = "new values"
a.save()

# delete
a.delete()

# to filter data
model_name.objects.filter(field1 = "...", field2 = "...", ....)