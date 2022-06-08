"""learning_losのURLパターンの定義"""

from django.urls import path

from . import views

app_name = 'learning_los'
urlpatterns = [
  # ホームページ
  path('', views.index, name='index'),
  # すべてのトピックを表示するページ
  path('topics/', views.topics, name="topics"),
]