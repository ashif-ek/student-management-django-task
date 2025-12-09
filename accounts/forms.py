from django import forms
from .models import CustomUser, StudentProfile
from django.contrib.auth.forms import UserCreationForm

class CustomUserRegisterForm(UserCreationForm):
    role = forms.ChoiceField(choices=[('STUDENT', 'Student'), ('ADMIN', 'Admin')])

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'role']


class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['roll_number', 'department', 'year_of_admission']
