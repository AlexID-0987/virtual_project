from django.shortcuts import render
from django import forms 
from django.http import HttpResponseRedirect 
from django.urls import reverse
# Create your views here.
#tasks=[]
class NewTaskForms(forms.Form):
    task=forms.CharField(label="New Task")
    priority=forms.IntegerField(label='Priority',min_value=1,max_value=10)
def index(request):
    if 'tasks' not in request.session:
        request.session['tasks']=[]
    return render(request, 'task/index.html',{
        'myDay':request.session['tasks']
    }) 
def add(request):
    if request.method=='POST':
        form=NewTaskForms(request.POST)
        if form.is_valid():
            task=form.cleaned_data['task']
            request.session['tasks']+=[task]
            #return HttpResponseRedirect(reverse('task:index'))   
        else:
            return render(request, 'task/add.html',{
                'form':form
            })
    return render(request, "task/add.html",{
        'form':NewTaskForms()
    })