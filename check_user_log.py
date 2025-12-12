import os
import django
import sys

# Redirect stdout to a file
sys.stdout = open('users_output.txt', 'w')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth import get_user_model
User = get_user_model()

email = "ashifek11@gmail.com"
exists = User.objects.filter(email=email).exists()
print(f"User with email {email} exists: {exists}")

print("Listing all users:")
for u in User.objects.all():
    print(f"  {u.username}: {u.email}")
