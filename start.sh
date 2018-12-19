python3 manage.py migrate
python3 manage.py shell -c 'from django.contrib.auth.models import User
user=User.objects.create_user("bridges", password="superbridges")
user.email="email@email.com"
user.is_superuser=True
user.is_staff=True
user.save()'
python3 manage.py runserver 0.0.0.0:8000

