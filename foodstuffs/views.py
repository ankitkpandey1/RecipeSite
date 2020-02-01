from django.shortcuts import render
from foodstuffs.forms import UserForm,LoginForm, MakeRecipeForm, EditRecipeForm, SearchForm
from django.contrib import sessions
from django.shortcuts import redirect
from django.utils import timezone
from django.http import HttpResponse
from .models import User, UserRecipe 



'''base function is for initialization of session variables only. '''


''' q subscript and variable name denotes a query '''

def base(request):
    try:
        test1=request.session['is_logged']
        test2=request.session['id']
    except:
        request.session['is_logged']=False
        request.session['id']=-1
   
    return redirect('/foodstuffs')
    
  
''' in case of deletion of all records, please delete sqllite file too as it can create nasty errors '''
def home(request):
       
    islog=request.session['is_logged']
    userq=''
  
    if islog == True and request.session['id'] != -1:
        userq=User.objects.get(pk=request.session['id'])
    
    if request.method == "POST":
        form=SearchForm(request.POST)
        if form.is_valid():
            choice=form.cleaned_data.get("choice")
            keyword=form.cleaned_data['keyword']
            if(choice=="name"):
                q=UserRecipe.objects.filter(recipe_name__icontains=keyword)
            else:
                q=UserRecipe.objects.filter(recipe_ingredients__icontains=keyword)
           
            if q.first() is None:
                msg="Couldn't find any match!"
                return render(request,'foodstuffs/landingpage.html',{'msg':msg})
                
                   
            return render(request,'foodstuffs/searchresult.html',{'q':q})
    else:
        form=SearchForm()
    return render(request,'foodstuffs/home.html',{'form':form,'islog':islog,'userq':userq})
 

def recipe(request, recipe_id):
    try:
        userq=''
        q=UserRecipe.objects.get(pk=recipe_id)
        if request.session['is_logged'] == True:
            userq=User.objects.get(pk=request.session['id'])
    except:
        msg="Fatal Error"
        return render(request,'foodstuffs/landingpage.html',{'msg':msg})
    islog=request.session['is_logged']
    return render(request,'foodstuffs/recipe.html',{'q':q,'userq':userq, 'islog':islog})
        

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
                msg="Unable to log you in. Please try again."
                return render(request,'foodstuffs/landingpage.html',{'msg':msg})
        
    else:
        form=LoginForm()
    return render(request,'foodstuffs/login.html',{'form':form})

def logout(request):
    request.session['is_logged']=False
    request.session['id']=-1
    return redirect('/foodstuffs/success')

def makerecipe(request):
    if request.session['is_logged']==False:
        msg="Please login first"
        return render(request,'foodstuffs/landingpage.html',{'msg':msg})
    
    islog=request.session['is_logged']
    userq=''
  
    if islog == True:
        userq=User.objects.get(pk=request.session['id'])   
    
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
                msg="Sorry, unable to create recipe. Please contact administrator."
                return render(request,'foodstuffs/landingpage.html',{'msg':msg})
     
    else:
        form=MakeRecipeForm()
    return render(request,'foodstuffs/makerecipe.html',{'form':form,'userq':userq,'islog':islog})

def editrecipe(request, recipe_id):
    if request.session['is_logged']==False:
        msg="Please login first."
        return render(request,'foodstuffs/landingpage.html',{'msg':msg})
    q=UserRecipe.objects.get(pk=recipe_id)
    userq=User.objects.get(pk=request.session['id'])
    if q.user.id != userq.id:
        msg="Sorry, you don't have permission to do this operation. Please contact administrator."
        return render(request,'foodstuffs/landingpage.html',{'msg':msg})
        
    if request.method == "POST":
        form=EditRecipeForm(request.POST ,request.FILES)
        if form.is_valid():
            try:
                q=UserRecipe.objects.get(pk=recipe_id)
                if (form.cleaned_data['recipe_name'] != 'please fill in details'):
                    q.recipe_name=form.cleaned_data['recipe_name']
                if (form.cleaned_data['recipe_description'] != 'please fill in details'):
                    q.recipe_description=form.cleaned_data['recipe_description']
                if (form.cleaned_data['recipe_ingredients'] != 'please fill in details'):
                    q.recipe_ingredients=form.cleaned_data['recipe_ingredients']
                if (form.cleaned_data['recipe_steps'] != 'please fill in details'):
                    q.recipe_steps=form.cleaned_data['recipe_steps']
                if (form.cleaned_data['recipe_img'] != 'please fill in details'):
                    q.recipe_img=form.cleaned_data['recipe_img']
                                  
                      
                q.recipe_edit=timezone.now()
                q.save()
                return redirect('/foodstuffs/success')
            except:
                msg="Unable to do edit. Please contact administrator."
                return render(request,'foodstuffs/landingpage.html',{'msg':msg})
    else:
        form1=EditRecipeForm()
        q=UserRecipe.objects.get(pk=recipe_id)
        
    return render(request,'foodstuffs/editrecipe.html',{'form1':form1, 'q':q})

def success(request):
    return render(request,'foodstuffs/success.html')

def about(request):
    return render(request,'foodstuffs/about.html')

def profile(request):
    if request.session['is_logged']==False:
        msg="Please login first."
        return render(request,'foodstuffs/landingpage.html',{'msg':msg})
    userq=User.objects.get(pk=request.session['id']) 
    q=UserRecipe.objects.filter(user=userq) 
    
    return render(request,'foodstuffs/profile.html',{'userq':userq ,'q':q})
    