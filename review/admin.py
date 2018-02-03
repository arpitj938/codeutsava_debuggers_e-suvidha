from django.contrib import admin
from .models import *

class review_dataAdmin(admin.ModelAdmin):
	list_display=["review_id","location_id","infrastructure","hygiene","safety","overall","date","time","review","feedback"]

admin.site.register(review_data,review_dataAdmin)

# Register your models here.
