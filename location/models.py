from __future__ import unicode_literals
from django.db import models


class location_data(models.Model):
	location_id = models.IntegerField(primary_key=True,blank=False,null=False)
	lattitude = models.FloatField(max_length=300,blank=False,null=False)
	longitude = models.FloatField(max_length=300,blank=False,null=False)
	location_name = models.CharField(max_length=300,default="Swachh Public Toilet")
	location_address = models.CharField(max_length=600,blank=False,null=False)
	infrastructure = models.FloatField(blank = True,null= True,default=0)
	hygiene = models.FloatField(blank = True,null= True,default=0)
	safety = models.FloatField(blank=True,null = True,default=0)
	m = models.IntegerField(default=1)
	f = models.IntegerField(default=1)
	hours = models.CharField(max_length=300,default="5AM 10PM")
	overall = models.FloatField(blank= True,null=True,default=0)
	review_count = models.IntegerField(default=0)
	bad_count = models.IntegerField(default=0)

	def __str__(self):
		return "%s" % (self.location_id)


class images_data(models.Model):
	location_id = models.ForeignKey(location_data,on_delete=models.CASCADE)
	image_url = models.ImageField(upload_to='media/',default="media/default.img")
# Create your models here.
