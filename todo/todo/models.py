from multiprocessing.spawn import import_main_path
from django.db import models

# title, description, created, complete, important
# (문자, 문자, 날짜, 불린, 불린)

class Todo(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    important = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title