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
