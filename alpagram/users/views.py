from django.shortcuts import render,redirect

from .forms import RegisterForm
from django.contrib.auth import authenticate,login







# 기존 방식 - 지금은 사용하지 않음
def register(request):
    """
    회원가입 - post
    """
    if request.method == "POST":
        # RegisterForm 이용
        # 회원가입 완료 후 로그인 처리까지
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # 비밀번호 따로 저장
            user.set_password(form.cleaned_data['password'])
            user.save()

            # 로그인 처리
            login_user = authenticate(username = form.cleaned_data['email'], password=form.cleaned_data['password'])

            login(request, login_user)
            return redirect("home")
    else:
        form = RegisterForm()
    return render(request, "home.html", {"form":form})