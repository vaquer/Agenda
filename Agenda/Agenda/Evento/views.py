# Create your views here.
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.models import User
from models import Event
from forms import EventForm

def Index(request):
	return render(request,'organizarte_home.html',{})
	#return render(request,'pruebaform.html',{})

def Huevos(request):
	mensaje ="huevos python"
	return render(request,"index.html",{
			'mensaje': mensaje
		})

def LogIn(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect("/huevos/")
	else:
		if request.method == 'POST':
			username = request.POST.get('username_login','')
			password = request.POST.get('password_login','')

			if username == '' or password =='':
				return HttpResponseRedirect("/error/")

			user_authenticated = auth.authenticate(username=username,password=password)

			if user_authenticated is not None:
				auth.login(request,user_authenticated)
				return HttpResponseRedirect("/huevos/")
			else:
				return HttpResponseRedirect("/error/") 
		else:
			return HttpResponseRedirect("/error/") 

def Register(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect("/huevos/")
	else:
		if request.method == 'POST':
			username=request.POST.get('username','')
			email=request.POST.get('email','')
			password=request.POST.get('password','')
			password2=request.POST.get('password2','')

			if username == '' or email == '' or password == '' or password2 == '':
				errors = 'Debes llenar completa la informacion de registro '
				errors = errors + request.POST['username'] + email + password + password
				return render(request,"organizarte_home.html",{
					'errors':errors,
					})

			if password != password2:
				errors = 'Las contrasenas no coinciden'
				return render(request,"organizarte_home.html",{
					'errors':errors,
					})

			new_user = User.objetcts.create_user(username=username,
				email=email,
				password=password)

			new_user.is_staff = True
			new_user.save()
		else:
			return HttpResponseRedirect("/error/")


def Error(request):
	return render(request, "organizarte_error.html")

# def LogOut(request):
# 	auth.logout(request)
# 	return HttpResponseRedirect("")

# def AddUser(request):
# 	if request.Method = 'POST':


# def NewEventCalendar(request):
# 	if request.Method = 'POST':
# 		EventF = EventForm(request.POST)
# 		if EventF.is_valid():
# 			return HtttpResponseRedirect("/calendar/")
# 	else:
# 		EventF = EventForm()

# 	return render(request,'',{
# 		'EventF': EventF
# 		})