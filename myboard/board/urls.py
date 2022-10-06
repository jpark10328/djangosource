from django.urls import path

from . import views

app_name = "board"

urlpatterns = [
    
    #### 질문

    # http://127.0.0.1:8000/board/
    path('',views.index, name="index"),

    # http://127.0.0.1:8000/board/1/
    path('<int:question_id>/',views.question_detail, name="question_detail"),
    
    # http://127.0.0.1:8000/board/question/create/
    path('question/create/',views.question_create, name="question_create"),

    # http://127.0.0.1:8000/board/question/modify/1/
    path('question/modify/<int:question_id>/',views.question_modify, name="question_modify"),

    # http://127.0.0.1:8000/board/question/delete/1/
    path('question/delete/<int:question_id>/',views.question_delete, name="question_delete"),

    ###### 답변 

    # http://127.0.0.1:8000/board/answer/create/1/
    path('answer/create/<int:question_id>/',views.answer_create, name="answer_create"),
    
    # http://127.0.0.1:8000/board/answer/modify/1/
    path('answer/modify/<int:answer_id>/',views.answer_modify, name="answer_modify"),
    
    # http://127.0.0.1:8000/board/answer/delete/1/
    path('answer/delete/<int:answer_id>/',views.answer_delete, name="answer_delete"),
]
