# ToDo App
## Installation
#### Clone the repository to your local machine:
``git clone your-git-repo``  
#### Install Python 3, if you don't have it installed:
* https://www.python.org/downloads/
#### Create and activate a virtual environment:
* `python3 -m venv env`
* `source env/bin/activate`
#### Install necessary packages:
* `pip install -r requirements.txt`
#### Create PostgreSQL database:
* https://www.postgresqltutorial.com/postgresql-getting-started/
#### Configure database in settings.py:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'your_db_name',
        'USER': 'your_username',
        'PASSWORD': 'your_pasword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
#### Run database migrations:
* `python manage.py migrate`
#### Create a superuser:
* `python manage.py createsuperuser`
## Usage
1. #### Run the application
    `python manage.py runserver` 
2. #### Go to browser and type `localhost:8000`
3. #### Available endpoints:
    `localhost:8000`
    `localhost:8000/login`
    `localhost:8000/logout`
    `localhost:8000/register`
    `localhost:8000/task`
    `localhost:8000/task-create`
    `localhost:8000/task-update`
    `localhost:8000/task-delete`

## Examples
![img.png](img.png)
