set -o errexit

pip install -r requirements.txt

python manage.py createsuperuser

python manage.py migrate