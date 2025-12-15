from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from accounts.utils import admin_required, student_required
from accounts.models import CustomUser
from .models import Course, Enrollment
from .forms import CourseForm, EnrollmentForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from django.utils import timezone
from django.contrib import messages


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
        form = CourseForm(request.POST, request.FILES)  
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


from accounts.models import CustomUser

@login_required
@admin_required
def course_enroll(request, id):
    course = get_object_or_404(Course, id=id)

    if request.method == "POST":
        user_id = request.POST.get("student_id")
        student = CustomUser.objects.get(id=user_id)

        Enrollment.objects.create(student=student, course=course)

        messages.success(request, "Student enrolled successfully.")
        return redirect('course_list')

    students = CustomUser.objects.filter(role="STUDENT")

    return render(request, 'courses/course_enroll.html', {
        'course': course,
        'students': students,
    })



@login_required
@student_required
def student_courses(request):
    enrollments = Enrollment.objects.filter(student=request.user)

    return render(request, 'courses/student_courses.html', {
        'enrollments': enrollments
    })




@login_required
@student_required
def complete_course(request, enrollment_id):
    enrollment = get_object_or_404(Enrollment, id=enrollment_id, student=request.user)
    
    enrollment.completed = True
    enrollment.completed_at = timezone.now()
    enrollment.save()

    messages.success(request, "Course marked as completed.")
    return redirect('student_courses')
