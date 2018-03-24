from django.db import models

class Cart(models.Model):
	productid = models.CharField(max_length=100)
	username = models.CharField(max_length=100,default='guest')
