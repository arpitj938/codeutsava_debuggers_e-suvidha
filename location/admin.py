from django.contrib import admin
from .models import *

class location_dataAdmin(admin.ModelAdmin):
	list_display=["location_id","location_name","location_address","lattitude","longitude","m","f","d","hours","infrastructure","hygiene","safety","overall","review_count","bad_count"]

admin.site.register(location_data,location_dataAdmin)

class images_dataAdmin(admin.ModelAdmin):
	list_display= ["location_id","image_url"]

admin.site.register(images_data,images_dataAdmin)

# Register your models here.
