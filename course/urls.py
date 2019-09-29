from django.urls import path
from course.views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
	path('course/<slug:slug>/', courses_detail),
	path('course/',courses_page, name='courses_page'),
]