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

def usage_graph(request):
	# location_id = request.POST.get('location')
	location_id = 4
	response_json = {}
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
	# response_json["success"] = True
	# response_json["message"] = "All data included"
	# print str(response_json)
	# return HttpResponse(str(response_json))
def date_graph(request):
	# location_id = request.POST.get('location')
	# start_date = request.POST.get('start_date')
	# end_data = request.POST.get('end_date')
	location_id = 4
	start_date = datetime.date(2018, 01, 03)
	print start_date
	end_date = datetime.date(2018, 02, 04)
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
		# hourgraph = make_hour_graph()


# Create your views here.
