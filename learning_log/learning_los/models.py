from django.db import models

class Topic(models.Model):
  """ユーザーが学んでいるトピックを表すモデル

  Args:
      models (_type_): Model

  Returns:
      _type_: Topic
  """
  
  text = models.CharField(max_length=200)
  data_added = models.DateTimeField(auto_now_add=True)

  def __str__(self) -> str:
    """モデルの文字列表現を返す

    Returns:
        str: Topic.text
    """
    return self.text
