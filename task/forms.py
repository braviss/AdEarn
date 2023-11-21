from django import forms
from task.models import Task




class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'url', 'description', 'report', 'category', 'service_name')