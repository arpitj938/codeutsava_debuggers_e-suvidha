from __future__ import unicode_literals

from django.db import models
from location.models import location_data


class incharge_data(models.Model):
	incharge_id = models.IntegerField(primary_key=True)
	incharge_name = models.CharField(max_length=200,blank=False,null=False)
	incharge_phone = models.CharField(max_length=10,blank=False,null=False)
	incharge_email = models.EmailField(blank=False,null=False)
	location_allocated = models.OneToOneField(location_data, on_delete=models.CASCADE)

# Create your models here.
