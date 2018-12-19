from django import forms

class Todoform(forms.Form):
	title=forms.CharField(widget=forms.TextInput(attrs={'placeholder':"enter a title"}))
 
class TodoListingForm(forms.Form):
	todo_name=forms.CharField(widget=forms.TextInput(attrs={'placeholder':"enter work name"}))
	todo_description=forms.CharField(widget=forms.Textarea())