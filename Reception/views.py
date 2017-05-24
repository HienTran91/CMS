from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
 
def dashboard(request):
	#response = HttpResponse()
	#if 'name' in request.session:
	#	response.write("<h1>Tiep tan</h1>")
	#	response.write("Xin chao tiếp tân quèn:" + request.session['name'])
	#return response
	return render(request,"reception/dashboard.html")
def schedule(request):
	return render(request,"reception/schedule.html")
def management(request):
	return render(request,"reception/management.html")
def laboratory(request):
	return render(request,"reception/laboratory.html")
