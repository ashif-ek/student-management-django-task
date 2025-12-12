from django.apps import AppConfig

class CoursesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'courses_mgmt'

    def ready(self):
        import courses_mgmt.signals  # noqa


