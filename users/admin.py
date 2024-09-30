from django.contrib import admin
from .models import LoginRecord

#管理画面でログイン記録を確認出来るよう設定
admin.site.register(LoginRecord)
