from django.db import models

# Create your models here.

# class student(models.Model):
#     name=models.CharField(max_length=50)
#     age=models.IntegerField()
#     fathername=models.CharField(max_length=50)


class UserProfile(models.Model):
    name=models.CharField(max_length=50)
    Email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    # password2=models.CharField(max_length=50)