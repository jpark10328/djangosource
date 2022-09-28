from django.contrib import admin
from .models import Question,Choice

# admin.site.register(Question)

# 관리자에서 관리하는 커스터마이징
# admin.StackedInLine, admin.TabularInLine
class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    
    list_display = ("question_text","pub_date")

    # fields = ['pub_date','question_text']
    fieldsets = [
        (None, {"fields":["question_text"]}),
        ("Date Information",{"fields":['pub_date']})
    ]
    inlines = [ChoiceInLine]
    
admin.site.register(Question,QuestionAdmin)
# admin.site.register(Choice)

