from django.urls import path
from task import views


urlpatterns = [
    path('task/', views.TaskListView.as_view(), name='task_list'),
    path('task/<int:pk>/', views.TaskDetailView.as_view(), name='task_detail'),
    # path('task/<int:pk>/up/', views.TaskUpView, name='task_up'),
]