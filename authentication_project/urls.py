
from django.contrib import admin
from django.urls import path,include
from sign_up_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , views.home  , name= 'homepage'),
    path('sign_up/' , include('sign_up_app.urls') ), 
]
