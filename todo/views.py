from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import TodoModel
from django.urls import reverse_lazy

#ToDoのメイン画面
class TodoMain(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = TodoModel.objects.all()  # object_listをコンテキストに追加
        return context

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
    success_url = reverse_lazy('main')

#ToDoの削除機能
class TodoDelete(DeleteView):
    template_name = 'todo/delete.html'
    model = TodoModel
    success_url = reverse_lazy('main')

#ToDoの編集機能
class TodoUpdate(UpdateView):
    template_name = 'todo/update.html'
    model = TodoModel
    fields = ('title', 'contents', 'priority', 'duedate')
    success_url = reverse_lazy('main')
