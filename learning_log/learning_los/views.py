from django.shortcuts import render

from .models import Topic

def index(request):
  """学習ノートのホームページに遷移する処理

  Args:
      request (_type_): request

  Returns:
      _type_: index.html
  """
  return render(request, 'learning_los/index.html')

def topics(request):
    """すべてのトピックを取得し、トピック一覧に遷移する処理

    Args:
        request (_type_): request

    Returns:
        _type_: topics.html
    """
    # すべてのトピックを作成順に取得する
    topics = Topic.objects.order_by('data_added')
    # htmlに渡すコンテキストにトピック一覧を指定
    context = {'topics': topics}
    return render(request, 'learning_los/topics.html', context)

def topic(request, topic_id):
    """トピック詳細ページに遷移する処理

    Args:
        request (_type_): request
        topic_id (_type_): Topic.id

    Returns:
        _type_: topic.html
    """
    # id指定したトピックを取得する
    topic = Topic.objects.get(id=topic_id)
    # トピックに紐づく記事(entry)の取得
    entries = topic.entry_set.order_by('-data_added')
    # htmlに渡すコンテキストに個別トピックと記事内容を渡す
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_los/topic.html', context)
