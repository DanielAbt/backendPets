# backend_exercise
IRobot_django_exercise

Backed for https://github.com/danilobassi8/backend-interview-exercise

backendPets is a backend in Django to use with Pets-app frontend application:

You can:
 - Create new Users. 
 - Create new pets.
 - list all pets created by users.
 - Delete pets (only if you are admin).

## Requirements
 * Ubuntu Linux 18.04 or higher version.
 * Python 3
 * virtualenv
 * git


## Run app locally:

```sh
 $ git clone https://github.com/DanielAbt/backendPets.git
 $ python3 -m venv backendPets
 $ cd backendPets/
 $ source bin/activate
 $ pip3 install -r backendpets/requirements.txt
 $ python3 backendpets/manage.py makemigrations
 $ python3 backendpets/manage.py migrate
 ```