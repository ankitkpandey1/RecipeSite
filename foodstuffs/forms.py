from django import forms
from foodstuffs.models import User, UserRecipe,Comment
from django.forms import ModelForm

class UserForm(ModelForm):
    user_password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields= ["user_name","user_password","user_mail"]

