from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib.auth import authenticate, login

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect("users:login")

            # 로그인 처리까지 구현한다면?
            # 아이디와 비밀번호 가져오기
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            # 인증
            user = authenticate(request,username=username,password=password)

            if user is not None:
                login(request, user)
            return redirect("board:index")
            
    else:
        form = UserForm()
    return render(request, "users/register.html", {"form":form})
