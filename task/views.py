from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from task.models import Task
from django.views.generic import (
    DetailView,
    ListView,
    CreateView,
)
from task.forms import TaskCreateForm


class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'tasks'
    paginate_by = 5

    def get_queryset(self):
        return Task.objects.filter(status=True).order_by('-order')


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskCreateForm
    template_name = 'task_create_form.html'
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Task created success, awaiting verification')
        return response

    def form_invalid(self, form):
        messages.error(self.request, 'Task created error')
        return super().form_invalid(form)


class TaskDetailView(DetailView):
    model = Task
    template_name = 'task_detail.html'


