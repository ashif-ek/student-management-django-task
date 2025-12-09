from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Student
from .forms import StudentForm
from accounts.utils import admin_required
from django.contrib.auth.decorators import login_required

@login_required
@admin_required
def student_list(request):
    students = Student.objects.order_by('-created_at')
    return render(request, 'students/student_list.html', {'students': students})


@login_required
@admin_required
def student_add(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Student added successfully.")
            return redirect('student_list')
    else:
        form = StudentForm()

    return render(request, 'students/student_add.html', {'form': form})


@login_required
@admin_required
def student_edit(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, "Student updated successfully.")
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)

    return render(request, 'students/student_edit.html', {'form': form})


@login_required
@admin_required
def student_delete(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()

    messages.warning(request, "Student deleted.")
    return redirect('student_list')
