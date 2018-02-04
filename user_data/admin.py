from django.contrib import admin

from .models  import *


class admin_dataAdmin(admin.ModelAdmin):
	list_display = ["admin_id","password","admin_fname","admin_lname","admin_email","admin_phone"]

admin.site.register(admin_data,admin_dataAdmin)

# Register your models here.
