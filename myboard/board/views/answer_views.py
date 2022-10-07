from django.http import HttpResponse
from django.shortcuts import redirect, render,get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from ..forms import AnswerForm, QuestionForm, CommentForm
from ..models import Question, Answer, Comment

@login_required(login_url='users:login')
def answer_create(request,question_id):
    """
    Answer 등록
    """
    question = get_object_or_404(Question,id=question_id)

    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.author = request.user
            answer.save()
            # 성공시 detail
            return redirect("board:question_detail",question_id=question_id)
    else:
        form = AnswerForm()
        
    return render(request, "board/question_detail.html",{"form":form,"question":question})

@login_required(login_url='users:login')
def answer_modify(request, answer_id):
    
    answer = get_object_or_404(Answer, pk=answer_id)

    if request.method == "POST":
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.save()
            return redirect("board:question_detail", question_id = answer.question.id)
    else:
        form = AnswerForm(instance=answer)
    return render(request, "board/answer_modify.html",{"form":form})

@login_required(login_url='users:login')
def answer_delete(request, answer_id):

    answer = get_object_or_404(Answer, pk=answer_id)

    answer.delete()
    return redirect("board:index")
