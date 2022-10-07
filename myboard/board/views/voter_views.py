from django.shortcuts import redirect, render,get_object_or_404
from django.contrib.auth.decorators import login_required
from ..models import Question, Answer

def vote_question(request, question_id):
    """
    질문 추천 등록 : 본인이 작성한 글은 추천하지 못하도록/성공-detail
    """
