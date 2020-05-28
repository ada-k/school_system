from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', views.index, name='home'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
]


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('home', views.index, name='home'),
#     path('news', views.news, name='news'),
#     path('message', views.news, name='message'),
#     path('', include('attendance.urls', namespace = 'attendance')),
# ]
