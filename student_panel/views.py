from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from accounts.utils import student_required

@login_required
@student_required
def student_dashboard(request):
    if request.user.role != "STUDENT":
        return redirect('admin_dashboard')

    return render(request, 'student_panel/dashboard.html')
