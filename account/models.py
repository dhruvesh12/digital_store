from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class user_extend(models.Model):
	users=models.ForeignKey(User, on_delete=models.CASCADE,null=True)
	phone_no= models.CharField(max_length=10)
	otp=models.IntegerField(default=0)

	def __str__(self):
		return self.phone_no


class feedback(models.Model):
	name=models.CharField(max_length=50)
	last=models.CharField(null=True,max_length=50)
	email=models.CharField(null=True,max_length=50)
	phone=models.CharField(null=True,max_length=10)
	message=models.TextField(blank=True, null=True)
	date = models.DateTimeField(auto_now_add=True, blank=True)
	

	def __str__(self):
		return self.name