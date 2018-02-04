from django.shortcuts import render
from .models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from review.views import send_mail


@csrf_exempt
def login(request):
	admin_id = str(request.POST.get('user_id'))
	password = str(request.POST.get('password'))
	print admin_id
	print password
	response_json = {}
	try:
		admin_row = admin_data.objects.get(admin_id= admin_id,password=password)
		response_json["error"] = False
		response_json["fname"] = str(admin_row.admin_fname)
		response_json["lname"] = str(admin_row.admin_lname)
		response_json["phone"] = str(admin_row.admin_phone)
		response_json["email"] = str(admin_row.admin_email)
		response_json["message"] = "Login Successfully"
	except Exception,e:
		print e
		response_json["error"] = True
		response_json["message"] = "Invaild Credentials"
	print str(response_json)
	return HttpResponse(str(response_json))


@csrf_exempt
def forgot_password(request):
	email = str(request.POST.get('email'))
	response_json = {}
	try:
		admin_id = admin_data.objects.get(email=email)
		url = str(request.scheme+'://'+request.get_host()+"/verify/"+str(admin_id))
		msg = "To verify click" + str(url)
		sub = "verify email"
		send_mail(email,msg,sub)
		response_json["error"] = False
		response_json["message"] = "Email sent to your Email ID"
	except Exception,e:
		print e
		response_json["error"] = True
		response_json["message"] = "Invalid Email ID"
	print str(response_json)
	return HttpResponse(str(response_json))

# def verify(request,value):
# 	admin_id = str(value)
# 	try:
# 		admin_row = 