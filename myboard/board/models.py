from django.db import models
from django.contrib.auth.models import User

# 질문(Question) 모델
# 제목(subject-200), 내용(content), created_at()
class Question(models.Model):
    subject = models.CharField(max_length=200,verbose_name="제목")
    content = models.TextField(verbose_name="내용")
    author = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name="작성자")
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="작성날짜")
    # modified_at 칼럼 추가
    modified_at = models.DateTimeField(auto_now=True,verbose_name="수정날짜")
   

    def __str__(self) -> str:
        return self.subject



# 답변(Answer) 모델
# question(질문과 외래키), 내용(content), created_at
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    content = models.TextField(verbose_name="내용")
    author = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name="작성자")
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="작성날짜")
    # modified_at 칼럼 추가
    modified_at = models.DateTimeField(auto_now=True,verbose_name="수정날짜")
    

# 댓글 - 작성자, 댓글내용, 댓글작성일시, 댓글 수정일시, 이 댓글이 달린 질문, 이 댓글이 달린 답변
class Comment(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name="작성자")
    content = models.TextField(verbose_name="댓글내용")
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="작성날짜")
    modified_at = models.DateTimeField(auto_now=True,verbose_name="수정날짜")
    question = models.ForeignKey(Question, on_delete = models.CASCADE,null=True, blank=True, verbose_name="질문")
    answer = models.ForeignKey(Answer, on_delete = models.CASCADE,null=True, blank=True, verbose_name="답변")
