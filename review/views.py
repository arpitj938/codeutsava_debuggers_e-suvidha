from django.shortcuts import render
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import EmailMessage,get_connection
from custom_key.models import *
from django.core.mail.backends.smtp import EmailBackend
from .models import *
from incharge.models import *
import os
from location.models import *

def send_mail(email,msg,sub):
	host=custom_key_data.objects.get(key='host').value
	print host
	port=custom_key_data.objects.get(key='port').value
	username=custom_key_data.objects.get(key='username').value
	password=custom_key_data.objects.get(key='password').value
	backend = EmailBackend(host=str(host), port=int(port), username=str(username),
		password=str(password), use_tls=True, fail_silently=True)
	EmailMsg= EmailMessage(sub,msg,'no-reply@gmail.com',bcc=[email],connection=backend)
	EmailMsg.content_subtype = "html"
	EmailMsg.send()

def alertincharge(location_id):
	try:
		incharge = incharge_data.objects.get(location_allocated=location_id)
		incharge_name = incharge.incharge_name
		incharge_email = incharge.incharge_email
		msg = str(email_key_data.objects.get(key="email_alert").value)
		location_name = str(location_data.objects.get(location_id=location_id).location_name)
		msg = msg %(location_name)
		sub = "Problem in "+ location_name 
		send_mail(incharge_email,msg,sub)
	except Exception ,e:
		print e,"alertincharge"

def calculate_new(count,previous,new):
	return ((count*previous)+new)/(count+1.0)

#Create Graph
def makelinegrpah(request,location):
	line_json = {}
	for o in review_data.objects.filter(location_id=location):
		temp_json=[]

def open_index(request):
	return render(request,'index1.html')

# Create your views here.
@csrf_exempt
def get_review(request):
	try:
		lattitude = str(request.POST.get("latitude"))
		longitude=str(request.POST.get("longitude"))
		print lattitude
		print longitude
		infrastructure = float(request.POST.get("infrastructure"))
		safety = float(request.POST.get("safety"))
		hygiene = float(request.POST.get("hygiene"))
		overall = float(request.POST.get("overall"))
		review = str(request.POST.get("review"))
		feedback = str(request.POST.get("feedback"))
		# name = request.POST.get("name")
		# print name
		try:
			print str(request.FILES.get('file'))
			image=request.FILES.get('file').name
			this_refrence_id=str(int(review_data.objects.all().last().review_id)+1)
			while True:
				try:
					folder = 'media/'+this_refrence_id+'/'
					os.mkdir(os.path.join(folder))
					break
				except Exception,e:
					print e
					this_refrence_id=str(int(this_refrence_id)+1)
			# full_filename = os.path.join(folder, image)
			# print "full name",full_filename
			#fout = open(folder+image, 'wb+')
			print "image=",image
			image = this_refrence_id+"/"+image
			fout = open(folder+image, 'w')
			file_content = request.FILES.get('file').read()
			#for chunk in file_content.chunks():
			fout.write(file_content)
			fout.close()
		except Exception,e:
			print e
			pass
		# lattitude = "21.244003"
		# longitude="81.617268"
		# infrastructure = 1.0
		# safety = 1.0
		# hygiene = 1.0
		# overall = 1.0
		# review = "bad"
		# feedback = "do something"
		try:
			lattitude = lattitude.split('"')[1]
			longitude = longitude.split('"')[1]
			print lattitude
			location_obj = location_data.objects.get(lattitude=lattitude,longitude=longitude)
			location_id = int(location_obj.location_id)
			previous_infra = float(location_obj.infrastructure)
			previous_hygiene = float(location_obj.hygiene)
			previous_safety = float(location_obj.safety)
			previous_over = float(location_obj.overall)
			previous_count = int(location_obj.review_count)
			new_infra = calculate_new(previous_count,previous_infra,infrastructure)
			new_hygiene = calculate_new(previous_count,previous_hygiene,hygiene)
			new_safety = calculate_new(previous_count,previous_safety,safety)
			new_overall = calculate_new(previous_count,previous_over,overall)
			new_count = previous_count+1
			bad_count = location_obj.bad_count
			if(overall<3):
				bad_count = bad_count +1
				if(bad_count>0):
					alertincharge(int(location_id))
			location = location_data.objects.get(location_id=location_id)
			setattr(location,"infrastructure",new_infra)
			setattr(location,"hygiene",new_hygiene)
			setattr(location,"safety",new_safety)
			setattr(location,"review_count",new_count)
			setattr(location,"bad_count",bad_count)
			setattr(location,"overall",new_overall)
			location.save()
			try:
				review_object = review_data.objects.create(location_id=int(location_id),infrastructure=infrastructure,hygiene=hygiene,
					safety=safety,overall=overall,review=review,feedback=feedback,image=image)
				review_object.save()
			except:
				review_object = review_data.objects.create(location_id=int(location_id),infrastructure=infrastructure,hygiene=hygiene,
					safety=safety,overall=overall,review=review,feedback=feedback)
				review_object.save()
		except Exception,e:
			print e,"get_review"
	except Exception ,e:
		print e,"get_review"
	response_json={"success":True,"message":"Thanks for the Feedback"}
	print str(response_json)
	return HttpResponse(str(response_json))

@csrf_exempt
def send_review(request):
	try:
		latitude = str(request.POST.get("latitude"))
		longitude = str(request.POST.get("longitude"))
		# latitude = "21.248471"	
		# longitude = "81.579622"
		location_row = location_data.objects.get(lattitude=latitude,longitude=longitude)
		response_json = {}
		temp_json = {}
		temp_json["hygiene"] = location_row.hygiene
		temp_json["infrastructure"] = location_row.infrastructure
		temp_json["overall"] = location_row.overall
		temp_json["safety"] = location_row.safety
		temp_json["reviews"] = []
		for o in review_data.objects.filter(location_id=location_row.location_id):
			review_string = str(o.review)
			temp_json["reviews"].append(review_string)
		temp_json["reviews"] = temp_json["reviews"][:15]
		temp_json["reviews"] = temp_json["reviews"][::-1]
		temp_json["images"] = []
		url =  str(request.scheme+'://'+request.get_host()+'/media')
		for o  in images_data.objects.all():
			# print "in image"
			if(str(o.location_id)==str(location_row.location_id)):
				# print str(o.image_url)
				temp_json["images"].append(url+'/'+str(o.image_url))
		# temp_json["images"].append("https://wallpaperbrowse.com/media/images/5611472-simple-images.png")
		# temp_json["images"].append("http://milewalk.com/wp-content/uploads/2014/07/Keep-it-simple.jpg")
		# temp_json["images"].append("https://t4.ftcdn.net/jpg/01/21/84/15/240_F_121841507_k8yG2UdVD6kmrBUWjpXWnHS7bVHd9Ydk.jpg")
		response_json["data"] = temp_json
		response_json["success"] = True
		response_json["message"] = "All data sent"
		print str(response_json)
		return HttpResponse(str(response_json))
	except Exception,e:
		response_json["success"] = False
		response_json["message"] = "Some problem occur"




	