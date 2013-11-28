from django.shortcuts import render_to_response,render
from django.http import HttpResponseRedirect
from django.contrib import auth
from forms import FormLogin,FormRegisterLogin

def Index(request):
	form_login = FormLogin()
	form_register = FormRegisterLogin

	return render(request,'organizarte_home.html',{
		'form_login': form_login,
		'form_register':form_register,
		})	

def LogIn(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect("/huevos/")
	else:
		if request.method == 'POST':
			form_login = FormLogin(request.POST)

			if(form_login.is_valid()):				
				username = form_login.clean_data('username_login')
				password = form_login.clean_data('password_login')			

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
			form_register = FormRegisterLogin(request.POST)
			
			if(form_register.is_valid()):
				username=form_register.clean_data('username')
				email=form_register.clean_data('email')
				password=form_register.clean_data('password')
				password2=form_register.clean_data('password2')							

				user_duplicate = User.objects.get(username=username)

				if user_duplicate:
					form_login = FormLogin()
					errors = 'El usuario especificado ya ha sido registrado'
					return render(request,"organizarte_home.html",{
						'errors':errors,
						})

				new_user = User.objects.create_user(username=username,
					email=email,
					password=password)

				new_user.is_staff = True
				new_user.save()

				return HttpResponseRedirect("/huevos/")
		else:
			return HttpResponseRedirect("/error/")
