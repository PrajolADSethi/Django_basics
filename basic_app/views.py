from django.shortcuts import render
from . models import Blog
# Create your views here.
def index(request):
    list1 = [1,2,3,4,5]
    blogs = Blog.objects.all()
    tech = Blog.objects.filter(category='Technology')
    print(blogs)
    context={
    'data' : 'Hello World',
    'time' : "20 July 2000",
    'list' : list1 ,
    'tech' : tech,
    'blogs': blogs
        }
    return render(request,'index.html',context=context)
