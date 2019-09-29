from django.urls import path
from account.views import *
from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [

	path('',home, name='home'),
	path('register/',register, name='register'),
	path('login/',login_page, name='login_page'),

	
	path('otp/',test,name='test'),
	
	
	
	path('change-password/<token>/',changePassword,name='changePassword'),
	path('contact/',contact_page,name='contact_page'),
]