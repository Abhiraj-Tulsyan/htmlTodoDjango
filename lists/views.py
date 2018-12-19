from django.shortcuts import render, redirect, get_object_or_404

from lists.models import Todolist,Todo
from lists.forms import Todoform, TodoListingForm
from django.http import HttpResponse

def index(request):
	print(request.user.is_authenticated)
	return render(request,'lists/index.html', { 'Todoform': Todoform() , 'Todolist' : Todolist.objects.all() })
  

def addTodolist(request):
	if request.method =="POST":
		form=Todoform(request.POST)
		if form.is_valid():
			print(request.POST['title'])
			newTodoList=Todolist( title= request.POST['title'])
			newTodoList.save()
			print(newTodoList)
			for todo in Todolist.objects.all():
				print(todo)
	return redirect('lists:index')

def details(request,todolist_id):
	todolist=get_object_or_404(Todolist,pk=todolist_id)
	return render(request,'lists/details.html',{'todolist': todolist, 'form': TodoListingForm()})


def addTodo(request, todolist_id):
	todolist=get_object_or_404(Todolist,pk=todolist_id)
	print(todolist)
	if request.method=="POST":
		form=TodoListingForm(request.POST)
		if form.is_valid():
			newTodo=Todo(todolist=todolist,title=request.POST['todo_name'],description=request.POST['todo_description'])
			newTodo.save()
	return redirect( 'lists:details', todolist_id=todolist_id )

def deleteTodo(request, todolist_id):
	if request.method== 'POST':	
		Todo.objects.filter(pk=request.POST['xname']).delete()
	return redirect('lists:details', todolist_id=todolist_id)

def deleteTodolist(request,todolist_id):
	if request.method=="POST":
		Todolist.objects.filter(pk=todolist_id).delete()
	return redirect('lists:index')