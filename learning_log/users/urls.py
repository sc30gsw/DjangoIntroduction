"""users用URLパターンの定義
"""

from django.urls import path, include

app_name = 'users'
urlpatterns = [
  # デフォルトの認証URLを取り込む
  path('', include('django.contrib.auth.urls')),
]