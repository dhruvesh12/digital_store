from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group
# Register your models here.
class productAdmin(admin.ModelAdmin):
	list_display = ('name','email','date')
	list_filter = ('date',)

admin.site.register(user_extend)
admin.site.register(feedback,productAdmin)