from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    data = Article.objects.all()
    return render(request,'article/index.html',{'data':data})
