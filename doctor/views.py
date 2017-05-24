from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
 
def index(request):
	response = HttpResponse()
	if 'name' in request.session:
		response.write("<h1>Bac Sy</h1>")
		response.write("Chao bac sy: "+ request.session['name'])
	return response