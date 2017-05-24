from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .forms import LoginForm
from .models import User
from django.http import HttpResponseRedirect
def login(request):
	if request.method == 'POST':
		response = HttpResponse()
		username = request.POST['username']
		password = request.POST['password']
		try:
			go  = User.objects.get(name=username)
			response.write("<h1>Đăng nhập</h1></br>")
			# if go == null:
			# 	response.write("Sai tên rồi ông ơi!</br>")
			if go.password != password:
				response.write("Sai pass rồi ông ơi!</br>")
				return response
			else:
				#request.session['name'] = go.id
				request.session['name'] = go.name
				#response.write("Chào mừng anh: " + request.session['name'] + "đã đến với e</br>")
				if go.role == 1: # neu la bac si
					return HttpResponseRedirect("/doctor/")
				else: #neu la tiep tan
					return HttpResponseRedirect("/reception/")
				#render(request,"home.html")
				#return render(request,"home.html")
		except Exception as e:
			response.write("Sai tên rồi ông ơi!</br>")
			return response	
	loginForm = LoginForm() 
	return render(request, 'login/login.html', {'form':loginForm})
