# from django.db import models

# from accounts.models import CustomUser

# class Student(models.Model):
#     user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
#     name = models.CharField(max_length=100)
#     roll_number = models.CharField(max_length=50, unique=True)
#     email = models.EmailField(unique=True)
#     department = models.CharField(max_length=100)
#     year_of_admission = models.IntegerField()


#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.roll_number} - {self.name}"
