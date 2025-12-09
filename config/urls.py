
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('admin-panel/', include('admin_panel.urls')),
    path('student-panel/', include('student_panel.urls')),
    path('student-mgmt/', include('student_mgmt.urls')),
    path('courses-mgmt/', include('courses_mgmt.urls')),
    path('', RedirectView.as_view(url='/accounts/login/'), name='home'),
]
