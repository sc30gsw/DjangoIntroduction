from django.contrib import admin

from .models import Topic, Entry

# Topicモデルを管理サイトに登録
admin.site.register(Topic)
# Entryモデルを管理サイトに登録
admin.site.register(Entry)
