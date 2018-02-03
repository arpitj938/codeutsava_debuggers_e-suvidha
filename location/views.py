from django.shortcuts import render
from .models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def near_location_json(request):
	latitude = str(request.POST.get("latitude"))
	print latitude
	longitude = str(request.POST.get("longitude"))
	print longitude
	# latitude = 21.263775
	# longitude = 81.60574
	latitude = float(round(float(latitude),2))
	longitude = float(round(float(longitude),2))
	print latitude
	print longitude
	locations_rows = location_data.objects.all()
	row = []
	for o in locations_rows:
		if((latitude + 0.01 == float(round(float(o.lattitude),2))) or (latitude - 0.01 == float(round(float(o.lattitude),2)))):
			if((longitude + 0.01 == float(round(float(o.longitude),2))) or (longitude - 0.01 == float(round(float(o.longitude),2)))):
				row.append(o)
	# rows = [o for o in locations_rows if  (((latitude + 0.01) == float(round(o.latitude, 2)) OR  ((latitude- 0.01) == float(round(o.latitude, 2)))) AND ((longitude+0.01) == float(round(o.longitude, 2)) OR (longitude- 0.01) == float(round(o.longitude, 2)))) ]
	response_json = {}
	response_json["data"] =[]
	for o in row:
		temp_json = {}
		temp_json["name"] = str(o.location_name)
		temp_json["address"] = str(o.location_address)
		temp_json["m"] = str(o.m)
		temp_json["f"] = str(o.f)
		temp_json["hours"] = str(o.hours)
		temp_json["latitude"] = float(o.lattitude)
		temp_json["longitude"] = float(o.longitude)
		temp_json["overall"] = str(o.overall)
		response_json["data"].append(temp_json)
	response_json["success"] = True
	response_json["message"] = "All nearby data sent"
	print str(response_json)
	return HttpResponse(str(response_json))

