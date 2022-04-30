from socket import fromshare
from django import forms

class CreateNewUser(forms.Form):
    firstName = forms.CharField(label="First name" , max_length=200)
    lastName = forms.CharField(label="Last name" , max_length=200)
    username = forms.CharField(label="Username" , max_length=200)
    email = forms.CharField(label="Email", max_length=200)

class CreateNewItem(forms.Form):
    itemName = forms.CharField(label="name" , max_length=200)
    itemLink = forms.CharField(label="link" ,max_length=200)
    itemPhoto = forms.CharField(label="itemphoto" , max_length=200)
