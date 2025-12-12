from django.core.mail import send_mail
from django.conf import settings
import sys
import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

try:
    print(f"Attempting to send email with: Host={settings.EMAIL_HOST}, Port={settings.EMAIL_PORT}, User={settings.EMAIL_HOST_USER}")
    send_mail(
        subject="Debug Test Email",
        message="Testing SMTP configuration.",
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=["ashifek11@gmail.com"],
        fail_silently=False,
    )
    print("SUCCESS: Email sent successfully.")
except Exception as e:
    print(f"FAILURE: {e}")
