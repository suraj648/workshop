from django.shortcuts import render , redirect
from .models import *
from .forms import ArticleForm

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


def categorised_article(request, pk):

    if pk == 0:
        articles = Article.objects.all()
        context = {
            'articles':articles,
            'Category':'all'
            }
    else:
        category = Category.objects.get(pk=pk)

        articles = Article.objects.filter(Category=category).all()

        context = {
            'articles':articles,
            'category':category,
        }

    return render(request,'article/category.html',context)


def post_article(request):
    form = ArticleForm()

    if request.method == "POST":
        form = ArticleForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            return redirect('article:single_article', pk = form.instance.id)

    context = {
        'form':form
    }
    return render(request,'article/article_form.html',context)