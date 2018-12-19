from django.db import models

# Create your models here.
class Todolist(models.Model):
	title=models.CharField(max_length=150)
	created_at=models.DateField(auto_now_add=True)

	def __str__(self):
		return self.title



class Todo(models.Model):
	todolist=models.ForeignKey(Todolist,on_delete=models.CASCADE)
	title=models.CharField(max_length=150)
	description=models.CharField(max_length=450)
	
	def __str__(self):
		return self.title
