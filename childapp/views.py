

# Create your views here.
from django.shortcuts import render,HttpResponse
from childapp import models
from .models import TodoListdata

# Create your views here.
def home(request):
    return render(request, 'home.html')

def addtodo(request):
    if request.method =='POST':
        title = request.POST['nametitle']
        description = request.POST['namedescription']
        
        new_tododata = TodoListdata(nametitle=title, namedescription=description)
        new_tododata.save()
        
    return render(request, 'addtodo.html')

def viewtodo(request):
    alltododata = TodoListdata.objects.all()
    
    return render(request, 'viewtodo.html', {'alltododata': alltododata})

