from django.shortcuts import render
from users.models import LoginRecord

def calendar_view(request):
    #ログイン履歴をカレンダーに表示
    login_records = LoginRecord.objects.filter(user=request.user)
    highlighted_dates = [record.login_date.strftime('%Y-%m-%d') for record in login_records]
    return render(request, 'calendar_app/calendar.html', {'highlighted_dates':highlighted_dates})