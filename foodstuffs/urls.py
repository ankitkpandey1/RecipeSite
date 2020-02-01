      
from django.urls import path

from foodstuffs import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.home,name='home'),
    path('<int:recipe_id>/', views.recipe ,name='recipe'),
    path('signup' ,views.signup, name='signup'),
    path('login', views.login ,name='log in'),
    path('logout',views.logout, name='log out'),
    path('makerecipe',views.makerecipe,name='make recipe'),
    path('<int:recipe_id>/editrecipe',views.editrecipe,name='edit recipe'),
    path('success',views.success,name='success'),
    path('about',views.about,name='about'),
    path('profile',views.profile,name='profile'),
]

''' Base in view returns home page only '''