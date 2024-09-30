from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from .models import LoginRecord

#シグナルの設定　ユーザーログイン時のシグナルを受信し記録する
@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    LoginRecord.objects.create(user=user)