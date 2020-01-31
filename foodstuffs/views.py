from django.shortcuts import render
from foodstuffs.forms import UserForm
from django.contrib import sessions
from django.shortcuts import redirect
from django.utils import timezone

def base(request):
    pass
    
  

def home(request):
    pass

 

def recipe(request, recipe_id):
    pass

def signup(request):

    if request.method == "POST":
        form=UserForm(request.POST)
        if form.is_Valid():
            form.save()
            return redirect('/Success/')
    else:
        form=UserForm()
    return render(request,'foodstuffs/signup.html',{'form':form})

def login(request):
    pass

def logout(request):
    pass

def makerecipe(request):
    pass

def editrecipe(request):
    pass

def success(request):
    return render(request,'foodstuffs/success.html')