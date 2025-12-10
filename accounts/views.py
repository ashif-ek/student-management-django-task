from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import CustomUserRegisterForm, StudentProfileForm

def register_view(request):
    if request.method == 'POST':
        user_form = CustomUserRegisterForm(request.POST)
        profile_form = StudentProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            messages.success(request, 'Registration successful. Please log in.')
            return redirect('login')

    else:
        user_form = CustomUserRegisterForm()
        profile_form = StudentProfileForm()

    return render(request, 'accounts/register.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)

            if user.role == 'ADMIN':
                return redirect('admin_dashboard')
            else:
                return redirect('student_dashboard')

        messages.error(request, 'Invalid username or password')

    return render(request, 'accounts/login.html')



def logout_view(request):
    logout(request)
    messages.info(request, 'Logged out successfully.')
    return redirect('login')



@login_required
def profile_view(request):
    profile = None
    if request.user.role == "STUDENT":
        profile = request.user.studentprofile

    return render(request, 'accounts/profile.html', {
        'profile': profile
    })


from django.core.mail import send_mail
from django.http import HttpResponse

def test_email(request):
    send_mail(
        subject="Test Email from Django + Brevo",
        message="If you received this, SMTP is working.",
        from_email=None,  # uses DEFAULT_FROM_EMAIL
        recipient_list=["ashifek11@gmail.com"],
        fail_silently=False,
    )
    return HttpResponse("Email sent successfully!")
