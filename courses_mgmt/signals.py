from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings

from .models import Enrollment


@receiver(post_save, sender=Enrollment)
def send_enrollment_email(sender, instance, created, **kwargs):
    if not created:
        return  # only on new enrollment

    student = instance.student
    course = instance.course

    if not student.email:
        return

    subject = "You have been enrolled in a new course"
    message = f"Hi {student.name},\n\nYou have been enrolled in: {course.title}."

    try:
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[student.email],
            fail_silently=True,
        )
    except Exception:
        # In real projects, log this
        pass
