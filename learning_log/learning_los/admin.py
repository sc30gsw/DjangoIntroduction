from django.contrib import admin

from .models import Topic

# Topicモデルを管理サイトに登録
admin.site.register(Topic)
