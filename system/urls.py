from django.urls import path
from . import views

app_name = 'system'

urlpatterns = [
    path('students', views.student, name='students'),
    path('staff', views.staff, name='staff'),
    path('structures', views.structures, name='structures'),
    path('gallery', views.gallery, name='gallery'),
    path('ground', views.school, name='ground'),
    path('student_query', views.student_query, name='student_query'),
    path('staff_query', views.staff_query, name='staff_query'),
    path('structures_query', views.structures_query, name='structures_query'),
    path('ground_query', views.ground_query, name='ground_query'),    
]