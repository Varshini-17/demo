from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
from models import *
from django.forms import ModelForm
from django.core.validators import MaxLengthValidator
class RegisterForm(forms.ModelForm):
	email = forms.EmailField(label='Enter email')
	password = forms.CharField(label='password', widget=forms.PasswordInput)
	class Meta:
		model=Register
		fields=["email","password"]
	def clean(self):
		email=self.cleaned_data['email']
		password=self.cleaned_data['password']
		temp={'email':email,'password':password	}
		return temp

class LoginForm(forms.Form):
	email = forms.EmailField(label='Enter email')
	password = forms.CharField(label='Password', widget=forms.PasswordInput)

class Post(forms.ModelForm):
	title=forms.CharField(label="Title",validators=[MaxLengthValidator(100)])
	description=forms.CharField(label="Description",validators=[MaxLengthValidator(250)])
	question=forms.CharField(label='Question',validators=[MaxLengthValidator(500)])
	answer=forms.CharField(label='Answer',validators=[MaxLengthValidator(1000)])
	class Meta:
		model=Post_it
		fields=["title","description",'question','answer']

class UpdatePost(forms.ModelForm):
	title=forms.CharField(label="Title",validators=[MaxLengthValidator(100)])
	description=forms.CharField(label="Description",validators=[MaxLengthValidator(250)])
	question=forms.CharField(label='Question',validators=[MaxLengthValidator(500)])
	answer=forms.CharField(label='Answer',validators=[MaxLengthValidator(1000)])
	class Meta:
		model=Post_it
		fields=['title',"description",'question','answer']
