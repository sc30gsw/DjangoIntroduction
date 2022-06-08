from django.shortcuts import render, redirect

from .models import Topic, Entry
from .forms import EntryForm, TopicForm

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

def new_topic(request):
    """新規トピック作成画面に遷移し、トピックを作成する処理

    Args:
        request (_type_): request

    Returns:
        _type_: new_topic.html
    """
    # リクエストがPOSTでない場合
    if request.method != 'POST':
        # データを送信しないため空のフォームを生成する
        form = TopicForm()
    # リクエストがPOSTの場合
    else:
        # POSTでデータが送信されるためフォームにデータを渡す
        form = TopicForm(data=request.POST)
        # 入力値にエラーがない場合
        if form.is_valid():
            # データを保存する
            form.save()
            return redirect('learning_los:topics')
        
    # 空または無効のフォームを表示する
    context = {'form': form}
    return render(request, 'learning_los/new_topic.html', context)

def new_entry(request, topic_id):
    """指定したトピックに記事を追加する処理

    Args:
        request (_type_): request
        topic_id (_type_): Topic.id

    Returns:
        _type_: new_entry.html
    """
    topic = Topic.objects.get(id=topic_id)
    # リクエストがPOSTでない場合
    if request.method != 'POST':
        # データを送信しないため空のフォームを生成する
        form = EntryForm()
    # リクエストがPOSTの場合
    else:
        # POSTでデータが送信されるためフォームにデータを渡す
        form = EntryForm(data=request.POST)
        # 入力値にエラーがない場合
        if form.is_valid():
            # フォームの値を一時保存する
            new_entry = form.save(commit=False)
            # 記事オブジェクトのtopic属性に記事が属するトピックを指定する
            new_entry.topic = topic
            # データを保存する
            new_entry.save()
            return redirect('learning_los:topic', topic_id=topic_id)
    
    # 空または無効のフォームを表示する
    context = {'topic': topic ,'form': form}
    return render(request, 'learning_los/new_entry.html', context)

def edit_entry(request, entry_id):
    """既存の記事を編集する処理

    Args:
        request (_type_): request
        entry_id (_type_): Entry.id

    Returns:
        _type_: edit_entry.html
    """
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    # リクエストがPOSTでない場合
    if request.method != 'POST':
        # 初回リクエスト時は現在の記事の内容がフォームに表示される
        form = EntryForm(instance=entry)
    # リクエストがPOSTの場合
    else:
        # POSTでデータが送信されるためフォームにデータを渡す
        form = EntryForm(instance=entry, data=request.POST)
        # 入力値にエラーがない場合
        if form.is_valid():
            # データを保存する
            form.save()
            return redirect('learning_los:topic', topic_id=topic.id)

    context = {'entry': entry,'topic': topic, 'form': form}
    return render(request, 'learning_los/edit_entry.html', context)