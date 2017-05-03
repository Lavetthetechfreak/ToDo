from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Todo

# Create your views here.
def index(request):
	todos = Todo.objects.all()
	context = {
	'todos':todos
	}
	
	#return HttpResponse('Hello World')
	return render(request,'index.html',context)
#def details(request):
	#todo = Todo.objects.get(id)
	#context = {
	#'todo':todo
	#}
	#return render(request,'details.html',context)
def add(request):
	if(request.method=='POST'):
		title = request.POST['title']
		text = request.POST['text']
		todo= Todo(title=title,text=text)
		todo.save()
		return redirect('/to_do_list')
	else:
		return render(request,'add.html')
		

