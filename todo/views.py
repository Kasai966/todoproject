from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import TodoModel
from users.models import LoginRecord
from django.urls import reverse_lazy

#ToDoのメイン画面
class TodoMain(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = TodoModel.objects.filter(is_completed=False)  # 完了タスク以外のobject_listをコンテキストに追加
        
        #ログイン履歴をカレンダーに表示
        login_records = LoginRecord.objects.filter(user=self.request.user)
        highlighted_dates = [record.login_date.strftime('%Y-%m-%d') for record in login_records]
        context['highlighted_dates'] = highlighted_dates
        return context

#ToDoの一覧表示機能
class TodoList(ListView):
    template_name = 'todo/list.html'
    model = TodoModel

#完了タスクの一覧表示機能
class CompletedTasks(ListView):
    template_name = 'todo/completed_tasks.html'
    model = TodoModel
    #完了済みのタスクを取得
    def get_queryset(self):
        return TodoModel.objects.filter(is_completed=True)

#ToDoの詳細表示機能
class TodoDetail(DetailView):
    template_name = 'todo/detail.html'
    model = TodoModel

#ToDoの作成機能
class TodoCreate(CreateView):
    template_name = 'todo/create.html'
    model = TodoModel
    fields = ('title', 'contents', 'priority', 'duedate')
    success_url = reverse_lazy('index')

#ToDoの削除機能
class TodoDelete(DeleteView):
    template_name = 'todo/delete.html'
    model = TodoModel
    success_url = reverse_lazy('index')

#ToDoの編集機能
class TodoUpdate(UpdateView):
    template_name = 'todo/update.html'
    model = TodoModel
    fields = ('title', 'contents', 'priority', 'duedate')
    success_url = reverse_lazy('index')

#ToDoの完了機能
def complete_task(request, task_id):
    task = get_object_or_404(TodoModel, id=task_id)
    task.is_completed = True
    task.save()
    return JsonResponse({'status':'success'})
