from django.shortcuts import redirect

def admin_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.role != "ADMIN":
            return redirect('student_dashboard')
        return view_func(request, *args, **kwargs)
    return wrapper


def student_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.role != "STUDENT":
            return redirect('admin_dashboard')
        return view_func(request, *args, **kwargs)
    return wrapper
