from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.Courses, name = 'home-page'),
    # path('admin/', admin.site.urls),
   ]