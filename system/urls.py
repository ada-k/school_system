from django.urls import path
from . import views

app_name = 'system'

urlpatterns = [
    path('students', views.student, name='students'),
    path('s_del', views.student_delete, name='s_del'),
    path('staff', views.staff, name='staff'),
    path('st_del', views.staff_delete, name='st_del'),
    path('structures', views.structures, name='structures'),
    path('sts_del', views.structure_delete, name='sts_del'),
    path('gallery', views.gallery, name='gallery'),
    path('ground', views.ground, name='ground'),
    path('g_del', views.ground_delete, name='g_del'),
    path('student_query', views.student_query, name='student_query'),
    path('staff_query', views.staff_query, name='staff_query'),
    path('structures_query', views.structures_query, name='structures_query'),
    path('ground_query', views.ground_query, name='ground_query'),    
    path('school', views.school, name='school'), 
]