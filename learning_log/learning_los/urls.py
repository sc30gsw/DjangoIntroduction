"""learning_losのURLパターンの定義"""

from django.urls import path

from . import views

app_name = 'learning_los'
urlpatterns = [
  # ホームページ
  path('', views.index, name='index'),
  # すべてのトピックを表示するページ
  path('topics/', views.topics, name="topics"),
  # トピック詳細を表示するページ
  path('topics/<int:topic_id>/', views.topic, name="topic"),
  # 新規トピック作成ページのURL
  path('new_topic/', views.new_topic, name="new_topic"),
]