from django.db import models

class family(models.Model):
    fist_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    life = models.BooleanField()
    male = models.BooleanField()
    

class friends(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    male = models.BooleanField()
