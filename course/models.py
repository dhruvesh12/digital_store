from django.db import models
from slugify import slugify
from django.contrib.auth.models import User
from django.utils import timezone

class category(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class courses(models.Model):
    course_name=models.CharField(max_length=100)
    category=models.ForeignKey(category, on_delete=models.CASCADE,null=True)
    objective=models.TextField(blank=True, null=True)
    requriment=models.TextField(blank=True,null=True)
    thumnail=models.ImageField(upload_to='courses_image/')
    video=models.FileField(upload_to='courses_video/')
    price=models.IntegerField(default=0)
    slug = models.SlugField()

    def __str__(self):
        return self.course_name

    
# Create your models here.
class comment(models.Model):
    comment_on=models.ForeignKey(courses,on_delete=models.CASCADE,  null=True)
    comment_from=models.ForeignKey(User,on_delete=models.CASCADE,  null=True)
    comments=models.TextField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "User: {} has commented on {}".format(self.comment_from, self.comment_on)