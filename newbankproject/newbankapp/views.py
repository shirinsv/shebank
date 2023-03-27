

# Create your views here.

from django.shortcuts import render
from .models import district
# Create your views here.
def homepage(request):
    return render(request,'homepage.html')

def district_name(request):
    # obj = district.objects.all(),{"dist":obj}
    return render(request,'homepage.html')
def return_homepage(request):
    return render(request,'returnpage.html')