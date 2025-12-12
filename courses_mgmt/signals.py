from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings

from .models import Enrollment


@receiver(post_save, sender=Enrollment)
def send_enrollment_email(sender, instance, created, **kwargs):
    if not created:
        return  # Only send email on first creation

    student = instance.student
    course = instance.course

    if not student.email:
        return

    # SAFE fallback: first_name → username
    display_name = student.first_name or student.username

    subject = f"You have been enrolled in {course.title}"
    message = (
        f"Hello {display_name},\n\n"
        f"You have been successfully enrolled in: {course.title}.\n"
        f"Log in to your dashboard to access your course materials."
    )

    try:
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[student.email],
            fail_silently=False,  # Better for debugging
        )
    except Exception as e:
        # In real projects: log this error
        print("Email error:", e)
