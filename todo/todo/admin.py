from django.contrib import admin
from .models import Todo


# 모델을 어드민을 통해서 다룰 수 있음
admin.site.register(Todo)
