from django import forms
from .models import Course, Enrollment
from accounts.models import CustomUser

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'thumbnail']



class EnrollmentForm(forms.ModelForm):
    student = forms.ModelChoiceField(
        queryset=CustomUser.objects.filter(role="STUDENT")
    )

    class Meta:
        model = Enrollment
        fields = ['student']
