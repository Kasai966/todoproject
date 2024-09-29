from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import TodoModel
from django.urls import reverse_lazy

#ToDoの一覧表示機能
class TodoList(ListView):
    template_name = 'todo/list.html'
    model = TodoModel

#ToDoの詳細表示機能
class TodoDetail(DetailView):
    template_name = 'todo/detail.html'
    model = TodoModel

#ToDoの作成機能
class TodoCreate(CreateView):
    template_name = 'todo/create.html'
    model = TodoModel
    fields = ('title', 'contents', 'priority', 'duedate')
    success_url = reverse_lazy('list')

#ToDoの削除機能
class TodoDelete(DeleteView):
    template_name = 'todo/delete.html'
    model = TodoModel
    success_url = reverse_lazy('list')

#ToDoの編集機能
class TodoUpdate(UpdateView):
    template_name = 'todo/update.html'
    model = TodoModel
    fields = ('title', 'contents', 'priority', 'duedate')
    success_url = reverse_lazy('list')
