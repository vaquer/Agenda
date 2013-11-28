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

class FormRegisterLogin(forms.Form):
	username = forms.CharField(label='Nombre',initial='Tu nombre',widget=forms.TextInput(attrs={
		'id':'username',
		}))
	email = forms.EmailField(label='Correo',initial='correo@correo.com',widget=forms.TextInput(attrs={
		'id':'email',
		}))
	password = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={
		'id':'email',
		}))
	password2 = forms.CharField(label='Confirmacion',widget=forms.PasswordInput(attrs={
		'id':'email',
		}))

	def clean_password(self):
		field_password = self.clean_data.get('password')
		field_password2 = self.clean_data.get('password2')

		if field_password != field_password2:
			raise form.ValitationForm("Las contrasenas deben coincidir")

		return field_password;
	

