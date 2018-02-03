from django.contrib import admin
from .models import *
from location.models import *
from django.core import urlresolvers

class incharge_dataAdmin(admin.ModelAdmin):
	list_display=["incharge_id","incharge_name","incharge_phone","incharge_email","location_allocated"]

admin.site.register(incharge_data,incharge_dataAdmin)


# Register your models here.
