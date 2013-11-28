# Create your views here.
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.models import User
from models import Event
from forms import EventForm

def Huevos(request):
	mensaje ="huevos python"
	return render(request,"index.html",{
			'mensaje': mensaje
		})

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