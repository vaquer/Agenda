from django import forms
from django.contrib.auth.models import User

class FormLogin(forms.Form):
	username_login = forms.CharField(widget=forms.TextInput(attrs={
		'class':'InputLogin',
		'id':'username_login',
		}))
	password_login = forms.CharField(widget=forms.PasswordInput( 
		attrs={
			'class':'InputLogin',
			'id':'password_login',
		}))
	identificadorform = forms.CharField(required=True,initial='form_login',widget=forms.HiddenInput())

class FormRegisterLogin(forms.Form):
	username = forms.CharField(required=True,label='Nombre',initial='Tu nombre',widget=forms.TextInput(attrs={
		'id':'username',
		}))
	email = forms.EmailField(required=True,label='Correo',initial='correo@correo.com',widget=forms.TextInput(attrs={
		'id':'email',
		}))
	password = forms.CharField(required=True,label='Password',widget=forms.PasswordInput(attrs={
		'id':'email',
		}))
	password2 = forms.CharField(required=True,label='Confirmacion',widget=forms.PasswordInput(attrs={
		'id':'email',
		}))
	identificadorform = forms.CharField(required=True,initial='form_registro',widget=forms.HiddenInput())

	def clean(self):
		cleaned_data=super(FormRegisterLogin,self).clean()
		
		field_user = cleaned_data.get('username')
		field_email = cleaned_data.get('email')
		field_password = cleaned_data.get('password')
		field_password2 = cleaned_data.get('password2')


		if field_password != field_password2:
			msg="Las contrasenas deben coincidir"
			self._errors['password2'] = self.error_class([msg])

			del cleaned_data['password2']
			
		if User.objects.filter(username=field_user):
			msg="Ya existe un usuario con este nombre"
			self._errors['username'] = self.error_class([msg])

			del cleaned_data['username']

		if User.objects.filter(email=field_email):
			msg="Ya se ha registrado este email"
			self._errors['email']=self.error_class([msg])

			del cleaned_data['email']			

		return cleaned_data;