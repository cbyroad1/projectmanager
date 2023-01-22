from dataclasses import fields
from django import forms
from .models import Project, Task, User
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm


class Projectform(ModelForm):
    class Meta:
        model = Project
        fields = ['project_title', 'description', 'due_date']

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30, widget=forms.PasswordInput())

class Taskform(ModelForm):
    class Meta:
        model = Task
        fields = ['project', 'title', 'description', 'due_date']

