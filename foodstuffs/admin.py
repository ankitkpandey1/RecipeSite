from django.contrib import admin
from .models import User, UserRecipe

'''Can be modified in /admin'''
admin.site.register(User)
admin.site.register(UserRecipe)