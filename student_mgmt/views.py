from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from accounts.models import CustomUser, StudentProfile
from accounts.utils import admin_required
from django.contrib.auth.decorators import login_required


@login_required
@admin_required
def student_list(request):
    students = StudentProfile.objects.all()
    return render(request, "students/student_list.html", {"students": students})


@login_required
@admin_required
def student_add(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        roll = request.POST['roll_number']
        dept = request.POST['department']
        year = request.POST['year']

        user = CustomUser.objects.create_user(
            username=username,
            email=email,
            password=password,
            role="STUDENT"
        )

        StudentProfile.objects.create(
            user=user,
            roll_number=roll,
            department=dept,
            year_of_admission=year
        )

        messages.success(request, "Student created successfully")
        return redirect("student_list")

    return render(request, "students/student_add.html")


@login_required
@admin_required
def student_edit(request, id):
    profile = get_object_or_404(StudentProfile, id=id)

    if request.method == "POST":
        profile.roll_number = request.POST['roll_number']
        profile.department = request.POST['department']
        profile.year_of_admission = request.POST['year']
        profile.save()

        messages.success(request, "Student updated successfully.")
        return redirect("student_list")

    return render(request, "students/student_edit.html", {"profile": profile})


@login_required
@admin_required
def student_delete(request, id):
    profile = get_object_or_404(StudentProfile, id=id)
    profile.user.delete()   
    profile.delete()

    messages.warning(request, "Student deleted successfully")
    return redirect("student_list")
