# Интернет-магазин зоотоваров
## .env file:
SECRET_KEY=""
POSTGRES_USER=""
POSTGRES_PASSWORD=""
POSTGRES_NAME=""
POSTGRES_HOST=""
POSTGRES_PORT=""
PGADMIN_DEFAULT_EMAIL=""
PGADMIN_DEFAULT_PASSWORD=""
## Подготовка проекта к запуску
- python -m venv venv
- pip install -r requirements.txt
- touch .env - добавить переменные окружения, перечисленные выше
- python manage.py collectstatic
- python manage.py makemigrations
- python manage.py migrate
