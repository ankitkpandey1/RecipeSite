from django import forms
from foodstuffs.models import User, UserRecipe,Comment
from django.forms import ModelForm

class UserForm(ModelForm):
    user_password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields= ["user_name","user_password","user_mail"]

class LoginForm(forms.Form):
    usr_name=forms.CharField(max_length=50)
    usr_password=forms.CharField(widget=forms.PasswordInput)
    

class MakeRecipeForm(forms.Form):
    recipe_name=forms.CharField(max_length=50)
    recipe_description=forms.CharField(max_length=500)
    recipe_ingredients=forms.CharField(max_length=500)
    recipe_steps=forms.CharField(max_length=2000)
    recipe_img=forms.ImageField()
    
class EditRecipeForm(forms.Form):
    recipe_name=forms.CharField(max_length=50,required=False)
    recipe_description=forms.CharField(max_length=500,required=False)
    recipe_ingredients=forms.CharField(max_length=500,required=False)
    recipe_steps=forms.CharField(max_length=2000,required=False)
    recipe_img=forms.ImageField(required=False)
     