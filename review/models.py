from __future__ import unicode_literals

from django.db import models
from location.models import *

class review_data(models.Model):
	review_id = models.AutoField(primary_key=True)
	location_id = models.IntegerField(blank =False,null=False)
	infrastructure = models.FloatField(default = 3.0)
	hygiene = models.FloatField(default = 3.0)
	safety = models.FloatField(default = 3.0)
	overall = models.FloatField(default=3.0)
	review = models.TextField(blank=True,null=True)
	feedback = models.TextField(blank=True,null=True)
	date = models.DateField(auto_now_add=True)
	time = models.TimeField(auto_now_add=True)
	image = models.ImageField(upload_to = 'media/',default="media/default.jpg")


# Create your models here.
