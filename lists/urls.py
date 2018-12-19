from django.urls import path
from lists import views

app_name='lists'

urlpatterns=[ 
 path('', views.index, name='index'),
 path('todolist/add', views.addTodolist, name='add_todolist'),
 path('todolist/details/<int:todolist_id>',views.details,name='details'),
 path('todolist/addtodo/<int:todolist_id>', views.addTodo,name='add_todo'),
 path('todolist/deletetodo/<int:todolist_id>', views.deleteTodo, name='delete_todo'),
path('todolist/deletetodolist/<int:todolist_id>' , views.deleteTodolist, name='delete_todolist') 
]