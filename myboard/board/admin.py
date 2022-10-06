from django.contrib import admin
from .models import Question

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('subject','created_at')
    search_fields = ['subject']


admin.site.register(Question, QuestionAdmin)