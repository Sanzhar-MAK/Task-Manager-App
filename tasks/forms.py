from django import forms
from .models import Task
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description','completed')


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User()
        fields = ["email", "username", "password_1", "password_2"]