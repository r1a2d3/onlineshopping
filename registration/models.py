from django.db import models

class Userdata(models.Model):
	userid = models.CharField(max_length=100,default='guest')
	password=models.CharField(max_length=20)
	email=models.CharField(max_length=50)
	mono=models.CharField(max_length=10)
