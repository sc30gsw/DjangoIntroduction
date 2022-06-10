from django.db import models
from django.contrib.auth.models import User
class Topic(models.Model):
  """ユーザーが学んでいるトピックを表すモデル

  Args:
      models (_type_): Topic

  Returns:
      _type_: Topic
  """
  
  text = models.CharField(max_length=200)
  data_added = models.DateTimeField(auto_now_add=True)
  owner = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self) -> str:
    """モデルの文字列表現を返す

    Returns:
        str: Topic.text
    """
    return self.text


class Entry(models.Model):
    """トピックに関して学んだ具体的な内容(記事内容)を表すモデル

    Args:
        models (_type_): Entry

    Returns:
        _type_: Entry
    """

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    data_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self) -> str:
        """モデルの文字列表現を返す

        Returns:
            str: Entry.text
        """

        # 記事のテキストが25文字を超える場合のみ末尾に「...」を付ける
        if len(self.text) > 25:
            return f"{self.text[:25]}..."
        
        return f"{self.text[:25]}"
