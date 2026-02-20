from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Todolist

# Create your views here.

def index(request):
   people = [
   {
      "username": "diya23",
      "age": 23,
      "contact": "9800000001"
   },
   {
      "username": "alex99",
      "age": 5,
      "contact": "9811111111"
   },
   {
      "username": "maya_dev",
      "age": 22,
      "contact": "9822222222"
   },
   {
      "username": "rohan_k",
      "age": 27,
      "contact": "9833333333"
   },
   {
      "username": "sita01",
      "age": 24,
      "contact": "9844444444"
   }
]

   
   context = {
      "heading": "Index Page",
      "para":"this is a index page. this is the first html page in django",
      "people": people
   }
   return render(request, 'index.html', context)

def home(request):
   return render(request, 'home.html')

# create url, function, templates, extend templates
# about-us, contact-us

def todolist(request):
   todolist = Todolist.objects
   tasks = todolist.all()           # Todolist.objects.all()
   total = tasks.count()
   completed = todolist.filter(status = True).count()
   incompleted = todolist.filter(status = False).count()
   
   context = {
      "tasks": tasks,
      "total":total,
      "completed": completed,
      "incomplete": incompleted
   }
   
   return render(request, 'todolist.html', context) 

def create_tasks(request):
   if request.method == 'POST':
      user_title = request.POST.get('title')
      user_description = request.POST.get('description')
      if user_title == '' or user_description == '':
         context = {
            "error":"Both fields are required"
         }
         return render(request,'create.html',context)
      Todolist.objects.create(title = user_title, description = user_description)
      return redirect('/todolist/')
   return render(request,'create.html')

def mark_complete(request,id):
   task = Todolist.objects.get(id = id)
   task.status = True
   task.save()
   return redirect('/todolist/')
   # first check if status is True or False
   # if True: change to False
   # if False: change to True


def edit(request, id):
   task = Todolist.objects.get(id = id)
   context = {"task":task}
   if request.method == "POST":
      user_title = request.POST.get('title')
      user_description = request.POST.get('description')
      task.title = user_title
      task.description = user_description
      task.save()
      return redirect('/todolist/')
      
   return render(request, 'edit.html', context)

def delete(request,id):
   task = Todolist.objects.get(id = id)
   task.delete()
   return redirect('/todolist/')

# {'title':"ram", 'description':"abc"}