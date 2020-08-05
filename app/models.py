from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Title(models.Model):
    name=models.CharField(max_length=250,unique=True)
    desc=models.CharField(max_length=200)
    img=models.TextField(max_length=300)

    def __str__(self):
        return self.name

class Question(models.Model):
    ques = models.CharField(max_length=200)
    last_updated= models.DateTimeField(auto_now_add=True)
    title=models.ForeignKey(Title,related_name='questions',on_delete= models.CASCADE)
    started_by=models.ForeignKey(User,related_name='questions',on_delete= models.CASCADE)
    views = models.PositiveIntegerField(default=0)

class Post(models.Model):
    ans = models.TextField(max_length=3000)
    question = models.ForeignKey(Question,related_name='posts',on_delete= models.CASCADE)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(null=True)
    created_by = models.ForeignKey(User,related_name='posts',on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User,null=True,related_name='+',on_delete=models.CASCADE)

class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    profile_image = models.FileField()
