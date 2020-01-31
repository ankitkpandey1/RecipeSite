from django.shortcuts import render
from foodstuffs.forms import UserForm,LoginForm, MakeRecipeForm, EditRecipeForm
from django.contrib import sessions
from django.shortcuts import redirect
from django.utils import timezone
from django.http import HttpResponse
from .models import User, UserRecipe ,Comment

def base(request):
    request.session['is_logged']=False
    request.session['user_id']=-1
    return redirect('/foodstuffs')
    
  

def home(request):
    pass

 

def recipe(request, recipe_id):
    pass

def signup(request):

    if request.method == "POST":
        form=UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/foodstuffs/success')
    else:
        form=UserForm()
    return render(request,'foodstuffs/signup.html',{'form':form})

def login(request):
    
    if request.method == "POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            try:
                
                usr_name=form.cleaned_data['usr_name']
                usr_password=form.cleaned_data['usr_password']
                q=User.objects.get(user_name=usr_name,user_password=usr_password)
                request.session['is_logged']= True
                request.session['id']=q.id
                return redirect('/foodstuffs/success')
            except:
                return HttpResponse("<h1>Invalid Details</h1>")
        
    else:
        form=LoginForm()
    return render(request,'foodstuffs/login.html',{'form':form})

def logout(request):
    request.session['is_logged']=False
    request.session['id']=-1
    return redirect('/foodstuffs/success')

def makerecipe(request):
    if request.session['is_logged']==False:
        return HttpResponse("<h1>Please login first</h1>")
    
    if request.method == "POST":
        form=MakeRecipeForm(request.POST ,request.FILES)
        if form.is_valid():
            try:
                recipename=form.cleaned_data['recipe_name']
                recipedescription=form.cleaned_data['recipe_description']
                recipeingredients=form.cleaned_data['recipe_ingredients']
                recipesteps=form.cleaned_data['recipe_steps']
                recipeimg=form.cleaned_data['recipe_img']
                userq=User.objects.get(pk=request.session['id'])
                q=UserRecipe(recipe_name=recipename,recipe_description=recipedescription,recipe_ingredients=recipeingredients,recipe_steps=recipesteps,recipe_img=recipeimg, user=userq,recipe_publish=timezone.now(),recipe_edit=timezone.now())
                q.save()
                return redirect('/foodstuffs/success')
            except:
                return HttpResponse("<h1>Fatal Error</h1>")
                
           
    else:
        form=MakeRecipeForm()
    return render(request,'foodstuffs/makerecipe.html',{'form':form})

def editrecipe(request, recipe_id):
    if request.session['is_logged']==False:
        return HttpResponse("<h1>Please login first</h1>")
    q=UserRecipe.objects.get(pk=recipe_id)
    userq=User.objects.get(pk=request.session['id'])
    if q.user.id != userq.id:
        return HttpResponse("<h1>Permission denied</h1>")
        
    if request.method == "POST":
        form=EditRecipeForm(request.POST ,request.FILES)
        if form.is_valid():
            try:
                q=UserRecipe.objects.get(pk=recipe_id)
                if (not form.cleaned_data['recipe_name'] is None):
                    q.recipe_name=form.cleaned_data['recipe_name']
                if (not form.cleaned_data['recipe_description'] is None):
                    q.recipe_description=form.cleaned_data['recipe_description']
                if (not form.cleaned_data['recipe_ingredients'] is None):
                    q.recipe_ingredients=form.cleaned_data['recipe_ingredients']
                if (not form.cleaned_data['recipe_steps'] is None):
                    q.recipe_steps=form.cleaned_data['recipe_steps']
                if (not form.cleaned_data['recipe_img'] is None):
                    q.recipe_img=form.cleaned_data['recipe_img']
                                  
                      
                q.recipe_edit=timezone.now()
                q.save()
                return redirect('/foodstuffs/success')
            except:
                return HttpResponse("<h1>Fatal Error</h1>")
    else:
        form1=EditRecipeForm()
        q=UserRecipe.objects.get(pk=recipe_id)
        
    return render(request,'foodstuffs/editrecipe.html',{'form1':form1, 'q':q})

def success(request):
    return render(request,'foodstuffs/success.html')