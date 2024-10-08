release: python manage.py migrate && python manage.py createuser
web: gunicorn config.wsgi:application --log-file -

