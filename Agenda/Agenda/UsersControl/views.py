from django.shortcuts import render_to_response,render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.models import User
from forms import FormLogin,FormRegisterLogin

def Index(request):
	if request.method == "POST":
		requestform = request.POST.get('identificadorform')

		if requestform == 'form_login':
			if request.user.is_authenticated():
				auth.logout(request)
				return HttpResponseRedirect("/huevos/")
			else:
				form_register = FormRegisterLogin()
				if request.user.is_authenticated():
					return HttpResponseRedirect("/huevos/")
				else:			
					form_login = FormLogin(request.POST)				

					if(form_login.is_valid()):				
						username = form_login.cleaned_data('username_login')
						password = form_login.cleaned_data('password_login')			

						user_authenticated = auth.authenticate(username=username,password=password)

						if user_authenticated is not None:
							auth.login(request,user_authenticated)
							return HttpResponseRedirect("/huevos/")
						else:
							return HttpResponseRedirect("/error/") 		

		elif requestform == 'form_registro':
			form_login = FormLogin()

			if request.user.is_authenticated():
				auth.logout(request)
				return HttpResponseRedirect("/huevos/")
			else:						
				form_register = FormRegisterLogin(request.POST)
				
				if(form_register.is_valid()):
					username=form_register.cleaned_data.get('username')
					email=form_register.cleaned_data.get('email')
					password=form_register.cleaned_data.get('password')
					password2=form_register.cleaned_data.get('password2')							

					new_user = User.objects.create_user(username=username,
						email=email,
						password=password)

					new_user.is_staff = True
					new_user.save()

					return HttpResponseRedirect("/huevos/")		
		else:
			form_login = FormLogin()
			form_register = FormRegisterLogin()

	else:
		form_login = FormLogin()
		form_register = FormRegisterLogin()

	return render(request,'organizarte_home.html',{
			'form_login': form_login,
			'form_register':form_register,
			})	