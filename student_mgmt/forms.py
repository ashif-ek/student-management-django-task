from django import forms
from .models import Student
from accounts.models import CustomUser

class StudentForm(forms.ModelForm):
    password = forms.CharField(required=True, widget=forms.PasswordInput)

    class Meta:
        model = Student
        fields = [
            'name', 'roll_number', 'email', 'department', 'year_of_admission', 'password'
        ]
