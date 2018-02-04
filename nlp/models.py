from __future__ import unicode_literals

from django.db import models


class nlp_data(models.Model):
	nlp_id = models.AutoField(primary_key=True)
	review = models.CharField(max_length=500,blank=True,null=True)
	problem = models.CharField(max_length=500,blank=True,null=True)

# Create your models here.
