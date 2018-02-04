from django.shortcuts import render
from review.models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect
from plotly.offline import plot
from plotly.graph_objs import Scatter,Layout,Line,Bar
import plotly.graph_objs as go
import datetime


@csrf_exempt
# def usage_graph(request):
# 	# location_id = request.POST.get('location_id')
# 	location_id = 4
# 	response_json = {}
# 	review_count = review_data.objects.filter(location_id=location_id).count()
# 	print review_count

def make_line_graph(x_array,y_overall_array,y_hygiene_array,y_infrastructure_array):
	overall = go.Scatter(
    x=x_array,
    y=y_overall_array,
    name='OverallScore'
    )

	infrastruture = go.Scatter(
	    x=x_array,
	    y=y_infrastructure_array,
	    name ="Infrastruture"
	    )
	hygiene = go.Scatter(
	    x=x_array,
	    y=y_hygiene_array,
	    name = "Hygiene"
	    )
	data = [overall,infrastruture,hygiene]
	fig = go.Figure(data=data)
	graph_str = plot(fig,show_link=True,auto_open=False,output_type='div' )
	# graph_str=plot([Scatter(x=x_array, y=y_array)],show_link=True,auto_open=False,output_type='div')
	return graph_str

def make_bar_graph(x_array,y_array):
	graph_str=plot([Bar(x=x_array, y=y_array)],auto_open=False,output_type='div')
	return graph_str

def usage_graph(request,value):
	location_id = int(value)
	x_array = []
	y_overall_array=[]
	y_infrastructure_array=[]
	y_hygiene_array=[]
	i=0
	for o in review_data.objects.filter(location_id=location_id):
		x_array.append(i)
		y_overall_array.append(float(o.overall))
		y_hygiene_array.append(float(o.hygiene))
		y_infrastructure_array.append(float(o.infrastructure))
		i=i+1
	linegraph = make_line_graph(x_array,y_overall_array,y_hygiene_array,y_infrastructure_array)
	return render(request,'index1.html',{'link1':str(linegraph),'heading':"Review Rating Graph"})	

@csrf_exempt
def usage_post_graph(request):
	location_id = request.POST.get('id')
	location_id = 4
	response_json = {}
	response_json["url"] = 'usage'+'/'+str(location_id)
	print str(response_json)
	return HttpResponse(str(response_json))


def date_graph(request,value):
	url = value.split('_')
	location_id = url[0]
	start_date = url[1]
	end_date = url[2]
	start_date = start_date.split("-")
	end_date = end_date.split("-")
	start_date = datetime.date(int(start_date[0]), int(start_date[1]), int(start_date[2]))
	print start_date
	end_date = datetime.date(int(end_date[0]), int(end_date[1]), int(end_date[2]))
	print (end_date-start_date).days
	count = []
	x_array = []
	if(start_date==end_date):
		for o in range(0,24):
			count.append(0)
			x_array.append(o)
		for o in review_data.objects.all():
			count[o.time.hour] = count[o.time.hour] + 1
		print count
	else:
		for o in range(0,(end_date-start_date).days):
			count.append(0)
			x_array.append(o)
		for o in review_data.objects.all():
			count[(start_date-o.date).days] = count[(start_date-o.date).days] +1
		print count
	bargraph = make_bar_graph(x_array,count)
	return render(request,'index1.html',{'link1':str(bargraph),'heading':"Usage Graph"})


@csrf_exempt
def date_post_graph(request):
	# location_id = request.POST.get('id')
	# start_date = request.POST.get('start_date')
	# end_date  = request.POST.get('end_date')
	location_id = 4
	start_date = "2018-01-12"
	end_date = "2018-02-10"
	response_json = {}
	response_json["url"] = 'date'+'/'+str(location_id)+'_'+str(start_date)+'_'+str(end_date)
	print str(response_json)
	return HttpResponse(str(response_json))
		# hourgraph = make_hour_graph()

def send_all_location(request):
	response_json = {}
	try:
		response_json["data"] = []
		for o in location_data.objects.all():
			temp_json = {}
			temp_json["location_id"] = o.location_id
			temp_json["location_name"] = str(o.location_name)
			temp_json["location_address"] = str(o.location_address)
			temp_json["images"] = ""
			url =  str(request.scheme+'://'+request.get_host()+'/media')
			print url
			try:
				temp_json["image"] = url+'/'+str(((images_data.objects.filter(location_id=o.location_id))[0]).image_url)
				print temp_json["image"]
				# temp_json["images"].append(url+'/'+i.image_url)
			except Exception,e:
				print e
				pass
			response_json["data"].append(temp_json)
		print str(response_json)
		response_json["success"] = True
		response_json["message"] = "All location data sent"
		return HttpResponse(str(response_json))
	except Exception,e:
		print e
		response_json["success"] = False
		response_json["message"] = "Some error occured"
		print str(response_json)
		return HttpResponse(str(response_json))


# def nlp():
# 	for o in review_data_objects.all():
# 		if(o.overall<2):
			


 


# Create your views here.
