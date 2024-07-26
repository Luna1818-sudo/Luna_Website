from django.db import models

class CustomUser(models.Model):
    username = models.CharField(max_length=150)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    Country = models.CharField(max_length=100)
    State = models.CharField(max_length=100)
    Age = models.IntegerField(default=0) 
    password = models.CharField(max_length=128)
    email = models.EmailField
