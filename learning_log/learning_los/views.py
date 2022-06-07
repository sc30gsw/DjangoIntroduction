from django.shortcuts import render

def index(request):
  """学習ノートのホームページに遷移する処理

  Args:
      request (_type_): request

  Returns:
      _type_: index.html
  """
  return render(request, 'learning_los/index.html')
