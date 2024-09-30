from django.shortcuts import render
from users.models import LoginRecord

def calendar_view(request):
    #ログイン履歴をカレンダーに表示
    login_records = LoginRecord.objects.filter(user=request.user)
    events = [{'title':'ログイン', 'start':record.login_date.strftime('%Y-%m-%d'),
               'color':'green'} for record in login_records]
    return render(request, 'calendar_app/calendar.html', {'events':events})
