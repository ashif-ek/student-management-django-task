import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth import get_user_model
User = get_user_model()

print(f"User Model: {User}")
users = User.objects.all()
print(f"Total users: {users.count()}")
for u in users:
    print(f" - {u.username} ({u.email}) Active={u.is_active}")
