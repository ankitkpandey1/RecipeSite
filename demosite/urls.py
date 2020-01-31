
from django.contrib import admin
from django.urls import path,include
from foodstuffs import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.base,name='base'),
    path('foodstuffs/' , include('foodstuffs.urls')),
    path('admin/', admin.site.urls),
]
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)