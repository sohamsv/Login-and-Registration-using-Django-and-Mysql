from django.db import models
from django.db.models.fields import FilePathField

class Newuser(models.Model):
    Username=models.CharField(max_length=150)
    Email=models.CharField(max_length=150)
    Pwd=models.CharField(max_length=150)
    Age=models.IntegerField()
    Gender=models.CharField(max_length=1)
    MartialStatus=models.CharField(max_length=150)
