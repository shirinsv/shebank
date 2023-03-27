from django.urls import path
from . import views

app_name='newbankapp'
urlpatterns=[
    path('homepage',views.homepage,name='homepage'),
path('return_homepage',views.return_homepage,name='return_homepage'),
    ]