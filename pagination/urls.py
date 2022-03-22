from django.contrib import admin
from django.urls import path
from pageapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('studentapi',views.StudentList.as_view()),
]