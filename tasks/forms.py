from django import forms
from .models import Task
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description','completed')


class UserLoginForm(AuthenticationForm):
     pass

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(
         widget=forms.EmailInput(
              attrs={
         "placeholder":"Email",
         "class": "registration-form-item registration-form-email",
         "autocomplete": "email"
    }), required=True)
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields["username"].widget.attrs.update({
                 "placeholder":"Username",
                 "class": "registration-form-item registration-form-username",
                 "autocomplete": "username"
            })
            self.fields["password1"].widget.attrs.update({
                 "placeholder":"Password",
                 "class": "registration-form-item registration-form-password",
                 "autocomplete": "current-password"
            })
            self.fields["password2"].widget.attrs.update({
                 "placeholder":"Confirm password",
                 "class": "registration-form-item registration-form-password",
                 "autocomplete": "current-password"
            })
    class Meta:
        model = User
        fields = ("email", "username", "password1", "password2")
    
        
        
    