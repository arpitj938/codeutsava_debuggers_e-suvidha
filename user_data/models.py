from __future__ import unicode_literals

from django.db import models

class admin_data(models.Model):
	admin_id = models.CharField(max_length=300,primary_key=True)
	password = models.CharField(max_length=300,blank=False,null=False)
	admin_fname = models.CharField(max_length=300,blank=True,null=True)
	admin_email = models.CharField(max_length=300,blank=True,null=True)
	admin_phone = models.CharField(max_length=300,blank=True,null=True)
	admin_lname = models.CharField(max_length=300,blank=True,null=True)


# Create your models here.
