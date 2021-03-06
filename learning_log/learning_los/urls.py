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
  # 新規記事の作成ページのURL
  path('new_entry/<int:topic_id>/', views.new_entry, name="new_entry"),
  # 記事の編集ページのURL
  path('edit_entry/<int:entry_id>/', views.edit_entry, name="edit_entry"),
]