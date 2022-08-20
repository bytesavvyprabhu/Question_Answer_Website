from pyexpat import model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm,UserChangeForm,UserModel
from .models import User,question_model, answer_model
from django import forms
from django.forms.models import ModelForm
from django.forms.widgets import FileInput

from django import forms

class RegisterUserForm(ModelForm):
    class Meta:
        model = User
        fields = ['full_name', 'date_of_birth', 'contact_number', 'about', 'company_name', 'designation']
            

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['full_name', 'date_of_birth', 'contact_number', 'about', 'company_name', 'designation']
        exclude = ['user']
        widgets = {
         'profile_img': FileInput(),
         }

class ProfileUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = '__all__'


class question_form(forms.ModelForm):
    class Meta:
        model = question_model
        fields = '__all__'


class answer_form(forms.ModelForm):
    class Meta:
        model = answer_model
        fields = "__all__"

