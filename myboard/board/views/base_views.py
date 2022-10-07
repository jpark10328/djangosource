from django.http import HttpResponse
from django.shortcuts import redirect, render,get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from ..forms import AnswerForm, QuestionForm, CommentForm
from ..models import Question, Answer, Comment

def index(request):
    """
    Question 질문목록 추출
    """

    # 사용자가 요청한 페이지 값 가져오기
    page = request.GET.get("page", 1)

    # 전체 목록 추출
    question_lists = Question.objects.order_by("-created_at")

    # 전체 목록 안에서 사용자가 요청한 페이지에 대한 목록만 전송
    paginator = Paginator(question_lists, 10)
    question_list = paginator.get_page(page)

    return render(request, "board/question_list.html",{"question_list":question_list})


def question_detail(request,question_id):
    """
    Question 상세 내용 추출
    """
    question = get_object_or_404(Question, id=question_id)
    return render(request, "board/question_detail.html",{"question":question})
