from django.db import models

class register(models.Model):
    username=models.CharField(max_length=250)
    email=models.EmailField()
    gender=models.CharField(max_length=250)
    password=models.CharField(max_length=250)
    conformpassword=models.CharField(max_length=250)
    phone=models.IntegerField()




# Create your models here.
