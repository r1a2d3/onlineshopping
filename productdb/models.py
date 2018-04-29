from django.db import models
class Product(models.Model):
	productid = models.CharField(max_length=100)
	price = models.IntegerField()
	qty= models.IntegerField()
	url = models.CharField(max_length=1000000)
	pname = models.CharField(max_length=1000,default="")
	category=models.CharField(max_length=1000,default='')
