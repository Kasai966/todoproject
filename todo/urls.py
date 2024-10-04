from django.urls import path, include
from todo.views import SignUp, TodoMain, TodoList, TodoDetail, TodoCreate, TodoDelete, TodoUpdate, CompletedTasks
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='todo/login.html'), name='login'),
    path('index/', TodoMain.as_view(), name='index'),
    path('list/', TodoList.as_view(), name='list'),
    path('detail/<int:pk>', TodoDetail.as_view(), name='detail'),
    path('create/', TodoCreate.as_view(), name='create'),
    path('delete/<int:pk>', TodoDelete.as_view(), name='delete'),
    path('update/<int:pk>', TodoUpdate.as_view(), name='update'),
    path('complete/', CompletedTasks.as_view(), name='completed_tasks'),
    path('tasks/complete/<int:task_id>/',views.complete_task, name='complete_task'),
]

