from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
  """新規ユーザー登録を行う処理

  Args:
      request (_type_): request
  """
  # リクエストがPOSTでない場合
  if request.method != 'POST':
    # 空のユーザー登録フォームを表示する
    form = UserCreationForm()
  # リクエストがPOSTの場合
  else:
    # 入力済みのフォームを処理する
    form = UserCreationForm(data=request.POST)
    if form.is_valid():
      new_user = form.save()
      # ユーザーをログインさせてホームページにリダイレクトする
      login(request, new_user)
      return redirect('learning_los:index')
  
  context = {'form': form}
  return render(request, 'registration/register.html', context)