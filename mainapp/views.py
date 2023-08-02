from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, DetailView

from .forms import NewTaskForm
from .models import Task


class MainPageView(TemplateView):
    template_name = 'mainapp/index.html'


class NewTaskPAgeView(CreateView):
    template_name = 'mainapp/new_task.html'
    form_class = NewTaskForm


class DetailTask(DetailView):
    model = Task
    template_name = 'mainapp/task_detail.html'
    context_object_name = 'task'
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["form"] = NewTaskForm()
    #     return context

    
