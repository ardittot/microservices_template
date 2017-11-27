pip install virtualenv

mkdir ~/Workspace/tutorial-flask-api-complete

cd ~/Workspace/tutorial-flask-api-complete

virtualenv venv

source ./venv/bin/activate

touch .env
echo 'export FLASK_APP="run.py"' >> .env
echo 'export APP_SETTINGS="development"' >> .env
echo 'export DATABASE_URL="postgresql://postgres:ditto3391@localhost:5432/testdb"' >> .env
source .env

pip install flask psycopg2 SQLAlchemy Flask-API Flask-SQLAlchemy Flask-Script Flask-Migrate suds-jurko

mkdir instance
touch instance/__init__.py
touch instance/config.py
## Create instance/config.py

mkdir app
touch app/__init__.py
## Create app/__init__.py

touch run.py
## Create run.py

touch app/models.py
## Create app/models.py

touch manage.py
## Create manage.py

python manage.py db init
python manage.py db migrate
python manage.py db upgrade

# Initialize github
git init
git remote add origin https://github.com/ardittot/microservices_template.git
# Commit new source codes
git add ./
git commit -m "First commit"
git push -f origin master
git pull https://github.com/ardittot/microservices_template.git




