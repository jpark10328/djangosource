from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404

from .models import Question

def index(request):
    """
    Question 질문목록 추출
    """
    question_list = Question.objects.order_by("-created_at")

    return render(request, "board/board_list.html",{"question_list":question_list})
