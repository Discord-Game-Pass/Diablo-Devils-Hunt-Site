python manage.py collectstatic --clear --no-input
exec gunicorn DHV4_Web.wsgi:application --bind 0.0.0.0:8080 --workers=4
