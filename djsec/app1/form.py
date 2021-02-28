from django import forms
from django.forms import formset_factory
from app1.models import *

#this form use by multiple function in user section

class alogin(forms.Form):
    user = forms.CharField(widget=forms.TextInput(attrs={'class':'aa' , 'placeholder':'enter your username...'}), label="enter user id", max_length=30)
    pwd = forms.CharField(widget=forms.PasswordInput(attrs={'class':'aa', 'placeholder':'enter your passwrod..'}), label="enter password", max_length=30)

