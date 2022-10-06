from django.db import models

# 질문(Question) 모델
# 제목(subject-200), 내용(content), created_at()
class Question(models.Model):
    subject = models.CharField(max_length=200,verbose_name="제목")
    content = models.TextField(verbose_name="내용")
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="작성날짜")

# 답변(Answer) 모델
# question(질문과 외래키), 내용(content), created_at
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    content = models.TextField(verbose_name="내용")
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="작성날짜")
