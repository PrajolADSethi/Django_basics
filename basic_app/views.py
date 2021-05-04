from django.shortcuts import render
from . models import Blog, Questions
from django.http import HttpResponse
# from django.template import loader
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

def new(request):
    #simple http return
    # line= "Hello views ...."
    # return HttpResponse(line)

    #without template
    # latest_question_list = Questions.objects.order_by('published')[:5]
    # output = ', '.join([q.question for q in latest_question_list])
    # return HttpResponse(output)

    #with template using loader module
    # latest_question_list = Questions.objects.order_by('published')[:5]
    # template = loader.get_template('basic_app/new.html')
    # context = {
    #     'latest_question_list': latest_question_list,
    # }
    # return HttpResponse(template.render(context, request))

    # with template using render module
    latest_question_list = Questions.objects.order_by('published')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'new.html', context)
def details(request, question_id):
    return HttpResponse("You are looking at question %s." %question_id)

def results(request,question_id):
    response= "The answer to your question is %s."
    return HttpResponse(response %question_id)

def vote(request,question_id):
    return HttpResponse("You are voting in a question %s." %question_id)
