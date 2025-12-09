from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounts.models import CustomUser
from accounts.utils import admin_required

@login_required
@admin_required
def admin_dashboard(request):
    if request.user.role != "ADMIN":
        return redirect('student_dashboard')

    return render(request, 'admin_panel/dashboard.html')
