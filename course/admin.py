from django.contrib import admin
from .models import *
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("course_name",)}
admin.site.register(category)
admin.site.register(courses,ArticleAdmin)
admin.site.register(comment)