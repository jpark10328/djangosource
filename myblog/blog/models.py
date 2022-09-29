from django.db import models
from user.models import User
from django.utils import timezone



# 글번호(자동-pk), 제목(30), 내용(TextField), 작성날짜(DateTime), 수정날짜, 작성자(User),
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30, blank=False)
    content = models.TextField(default='')
    image = models.ImageField(blank=True, null=True)
    # auto_now_add : (생성일자) - 최초 저장시만 현재날짜 삽입
    # auto_now : (수정일자) - 갱신될 때마다 날짜 삽입
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title