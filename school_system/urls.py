from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('home', views.index, name='home'),
    path('', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('', include('system.urls', namespace = 'system')),
]
