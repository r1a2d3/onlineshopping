from django.db import models
class Order(models.Model):
	userid = models.CharField(max_length=100,default='guest')
	name = models.CharField(max_length=100,default='SOME STRING')
	area = models.CharField(max_length=100,default='SOME STRING')
	buldingname = models.CharField(max_length=100,default='SOME STRING')
	landmark = models.CharField(max_length=100,default='SOME STRING')
	mobileno = models.CharField(max_length=11)
	productid = models.CharField(max_length=100, default='SOME STRING')
	ddate = models.DateField(blank=True)
	city = models.CharField(max_length=100,default='SOME STRING')
	state = models.CharField(max_length=100,default='SOME STRING')
	pincode = models.CharField(max_length=7)
	ordertime=models.DateTimeField(auto_now=True)
	
# Create your models here.
