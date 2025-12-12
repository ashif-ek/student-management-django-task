from django.core.mail import send_mail
from django.conf import settings
import sys
import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

# Try to use the recipient as the sender, assuming it's the verified account email
TEST_SENDER = "ashifek11@gmail.com"

try:
    print(f"Attempting to send email...")
    print(f"Host: {settings.EMAIL_HOST}")
    print(f"From: {TEST_SENDER} (Overriding settings.DEFAULT_FROM_EMAIL because existing one looks invalid)")
    print(f"To: ashifek11@gmail.com")
    
    send_mail(
        subject="Debug Test Email - Valid Sender",
        message="If you receive this, the issue was indeed the DEFAULT_FROM_EMAIL setting.",
        from_email=TEST_SENDER,
        recipient_list=["ashifek11@gmail.com"],
        fail_silently=False,
    )
    print("SUCCESS: Email sent successfully.")
except Exception as e:
    print(f"FAILURE: {e}")
