from django import forms
from .models import Course, Enrollment
from student_mgmt.models import Student

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description']


class EnrollmentForm(forms.ModelForm):
    student = forms.ModelChoiceField(queryset=Student.objects.all())

    class Meta:
        model = Enrollment
        fields = ['student']
