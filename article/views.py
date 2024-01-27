from django.shortcuts import render
from .models import *

# Create your views here.

# CONTEXT PROCESSOR  CATEGORY

def categories(request):
    categories = Category.objects.all()

    return {
        'categories':categories,
    }
        
    

def index(request):
    data = Article.objects.all()
    return render(request,'article/index.html',{'data':data})


def single_article(request,pk):


    article = Article.objects.get(pk=pk)

    context={
        "article":article,
    }

    return render(request,'article/article.html', context)