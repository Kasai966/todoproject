from django.db import models
from django.contrib.auth.models import AbstractUser

#カスタムユーザーモデルを定義
class CustomUser(AbstractUser):
    pass

#ログイン履歴を記録するモデル
class LoginRecord(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE) #カスタムユーザーを参照
    login_date = models.DateTimeField(auto_now_add=True)