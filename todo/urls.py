from django.urls import path, include
from todo.views import TodoMain, TodoList, TodoDetail, TodoCreate, TodoDelete, TodoUpdate
from . import views

urlpatterns = [
    path('index/', TodoMain.as_view(), name='index'),
    path('list/', TodoList.as_view(), name='list'),
    path('detail/<int:pk>', TodoDetail.as_view(), name='detail'),
    path('create/', TodoCreate.as_view(), name='create'),
    path('delete/<int:pk>', TodoDelete.as_view(), name='delete'),
    path('update/<int:pk>', TodoUpdate.as_view(), name='update'),
    #path('tasks/', views.task_list, name='task_list'),
    path('tasks/complete/<int:task_id>/',views.complete_task, name='complete_task'),
]

