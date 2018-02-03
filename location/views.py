from django.shortcuts import render
from .models import *
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def near_location_json(request):
	# latitude = models.POST.get("latitude")
	# longitude = models.POST.get("longitude")
	latitude = 21.263775
	longitude = 81.60574
	latitude = float("{0:.2f}".format(latitude))
	longitude = float("{0:.2f}".format(longitude))
	print latitude
	print longitude
	locations_rows = location_data.objects.all()
	for o in locations_rows:
		if((latitude + 0.01 == float(round(o.latittude,2))) or (latitude - 0.01 == float(round(o.latittude,2)))):
			if((longitude + 0.01 == float(round(o.longitude,2))) or (longitude - 0.01 == float(round(o.longitude,2)))):
				pass
	# rows = [o for o in locations_rows if  (((latitude + 0.01) == float(round(o.latitude, 2)) OR  ((latitude- 0.01) == float(round(o.latitude, 2)))) AND ((longitude+0.01) == float(round(o.longitude, 2)) OR (longitude- 0.01) == float(round(o.longitude, 2)))) ]
	response_json = {}
	for o in row:
		temp_json = {}
		temp_json["name"] = str(o.loaction_name)
		temp_json["address"] = str(o.loaction_address)
		temp_json["m"] = o.m
		temp_json["f"] = o.f
		temp_json["hours"] = str(o.hours)
		temp_json["latitude"] = o.latitude
		temp_json["longitude"] = o.longitude
		temp_json["overall"] = o.overall
		response_json["data"].append(temp_json)
	response_json["success"] = True
	response_json["message"] = "All nearby data sent"
	print str(response_json)
	return HttpResponse(str(response_json))

