from django.urls import path
from . import views

app_name='logbank'
urlpatterns=[
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
path('new',views.new,name='new'),
path('add_userdetails',views.add_userdetails,name='add_userdetails')]