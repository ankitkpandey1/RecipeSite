from django import forms
from foodstuffs.models import User, UserRecipe
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
    recipe_name=forms.CharField(max_length=50,widget=forms.Textarea(attrs={'cols':50,'rows':1}))
    recipe_description=forms.CharField(max_length=500,widget=forms.Textarea(attrs={'cols':50,'rows':5}) )
    recipe_ingredients=forms.CharField(max_length=500,widget=forms.Textarea(attrs={'cols':50,'rows':5}))
    recipe_steps=forms.CharField(max_length=2000,widget=forms.Textarea(attrs={'cols':50,'rows':10}))
    recipe_img=forms.ImageField()
    
    
    '''default values will be compared during editing operation in order filter out changes made in recipe'''
class EditRecipeForm(forms.Form):
    recipe_name=forms.CharField(max_length=50,required=False,initial='please fill in details')
    recipe_description=forms.CharField(max_length=500,required=False,initial='please fill in details')
    recipe_ingredients=forms.CharField(max_length=500,required=False,initial='please fill in details')
    recipe_steps=forms.CharField(max_length=2000,required=False,initial='please fill in details')
    recipe_img=forms.ImageField(required=False,initial='please fill in details')
    
class SearchForm(forms.Form):
    keyword=forms.CharField(max_length=50,widget=forms.Textarea(attrs={'cols':40,'rows':1}) )
    choice=forms.CharField(max_length=10)
    