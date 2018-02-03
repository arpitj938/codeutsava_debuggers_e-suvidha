from django.shortcuts import render
from review.models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect
from plotly.offline import plot
from plotly.graph_objs import Scatter, Layout,Line


@csrf_exempt
# def usage_graph(request):
# 	# location_id = request.POST.get('location_id')
# 	location_id = 4
# 	response_json = {}
# 	review_count = review_data.objects.filter(location_id=location_id).count()
# 	print review_count

def make_graph(x_array,y_array):
	graph_str=plot([Scatter(x=x_array, y=y_array)],auto_open=False,output_type='div')
	return graph_str


def usage_graph(request):
	# location_id = request.POST.get('location')
	location_id = 4
	response_json = {}
	response_json["x"] = []
	response_json["y"] = []
	i=0
	for o in review_data.objects.filter(location_id=location_id):
		response_json["x"].append(i)
		response_json["y"].append(float(o.overall))
		i=i+1
	graph = make_graph(response_json["x"],response_json["y"])
	return render(request,'index1.html',{'link1':str(graph)})	
	# response_json["success"] = True
	# response_json["message"] = "All data included"
	# print str(response_json)
	# return HttpResponse(str(response_json))


# Create your views here.
