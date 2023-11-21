from django.shortcuts import render
from task.models import Task
from django.views.generic import (
    DetailView,
    ListView,
    FormView,
)
# from task.forms import TaskUpForm


class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.filter(status=True).order_by('-created_at')


class TaskDetailView(DetailView):
    model = Task
    template_name = 'task_detail.html'



# class TaskUpView(FormView):
#     template_name = 'task_up.html'
#     form_class = TaskUpForm
#
#
