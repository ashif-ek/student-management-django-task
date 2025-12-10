from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from accounts.utils import admin_required, student_required
from accounts.models import CustomUser
from student_mgmt.models import Student
from .models import Course, Enrollment
from .forms import CourseForm, EnrollmentForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


@login_required
@admin_required
def course_list(request):
    # 1) search
    search_query = request.GET.get('q', '').strip()

    courses_qs = Course.objects.all().order_by('-created_at')

    if search_query:
        courses_qs = courses_qs.filter(title__icontains=search_query)

    # 2) pagination
    paginator = Paginator(courses_qs, 5)  # 5 courses per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'search_query': search_query,
    }
    return render(request, 'courses/course_list.html', context)

# @login_required
# @admin_required
# def course_list(request):
#     courses = Course.objects.order_by('-created_at')
#     return render(request, 'courses/course_list.html', {'courses': courses})

@login_required
@admin_required
def course_add(request):
    if request.method == "POST":
        form = CourseForm(request.POST, request.FILES)  # request.FILES added
        if form.is_valid():
            form.save()
            messages.success(request, "Course added successfully.")
            return redirect('course_list')
    else:
        form = CourseForm()

    return render(request, 'courses/course_add.html', {'form': form})



@login_required
@admin_required
def course_edit(request, id):
    course = get_object_or_404(Course, id=id)

    if request.method == "POST":
        form = CourseForm(request.POST, request.FILES, instance=course)  # request.FILES added
        if form.is_valid():
            form.save()
            messages.success(request, "Course updated.")
            return redirect('course_list')
    else:
        form = CourseForm(instance=course)

    return render(request, 'courses/course_edit.html', {'form': form})


@login_required
@admin_required
def course_enroll(request, id):
    course = get_object_or_404(Course, id=id)

    if request.method == "POST":
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            enrollment = form.save(commit=False)
            enrollment.course = course
            enrollment.save()

            # SEND EMAIL HERE (next step)
            
            
            messages.success(request, "Student assigned to course.")
            return redirect('course_list')
    else:
        form = EnrollmentForm()

    return render(request, 'courses/course_enroll.html', {
        'course': course,
        'form': form
    })


@login_required
@student_required
def student_courses(request):
    student = get_object_or_404(Student, user=request.user)
    enrollments = Enrollment.objects.filter(student=student)

    return render(request, 'courses/student_courses.html', 
        {'enrollments': enrollments})
