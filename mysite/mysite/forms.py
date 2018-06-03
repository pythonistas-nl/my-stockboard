from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

# class LoginForm(forms.Form):
# 	username = forms.CharField(label='Username', max_length=100)
# 	password = forms.CharField(widget=forms.PasswordInput, label='Password', max_length=100)

# class RegisterForm(forms.Form):
# 	first_name = forms.CharField(label='First name', max_length=100)
# 	last_name = forms.CharField(label='Last name', max_length=100)
# 	username = forms.CharField(label='Username', max_length=100)
# 	password = forms.CharField(widget=forms.PasswordInput, label='Password', max_length=100)
# 	email = forms.CharField(widget=forms.EmailInput, label='Email', max_length=100)

class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = [User.username, User.password]

class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = [User.first_name, User.last_name, User.username, User.email, User.password]