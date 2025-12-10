from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('add/', views.course_add, name='course_add'),
    path('edit/<int:id>/', views.course_edit, name='course_edit'),
    path('enroll/<int:id>/', views.course_enroll, name='course_enroll'),
    path('my-courses/', views.student_courses, name='student_courses'),

]
