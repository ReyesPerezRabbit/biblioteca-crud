comandos para poder ejecutar el proyecto 

git init 

git remote add origin https://github.com/ReyesPerezRabbit/biblioteca-crud.git

git remote -v

git pull

git pull origin master

este no <git checkout master>

git checkout -b <como se llama la rama>

python -m venv venvBiblioteca
  
  verificar si estas en el entorno virtual 
  1: si marca error cambiar la terminal a cmd o bash

pip install -r requirements.txt

crear base de datos en pgadmin (db_crud) y mirar cambios en setting de bibliotecacrud si tan bien los datoss de base de datos y contraseñas 

python manage.py makemigrations

python manage.py migrate

python manage.py runserver
