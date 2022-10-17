from django.shortcuts import render,redirect, get_object_or_404

from users.models import CustomUser

from .forms import RegisterForm
from django.contrib.auth import authenticate,login
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from contents.models import Content, FollowRelation


@method_decorator(login_required, name="dispatch")
class ProfileView(TemplateView):
    """
    프로필 정보 보여주기 - 로그인 필요
    """
    template_name = "users/profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        contents = Content.objects.filter(user=self.request.user)
        context['contents'] = contents
        return context

@method_decorator(login_required, name="dispatch")
class GetView(TemplateView):
    """
    사용자가 요청한 user에 대한 정보를 추출
    """
    template_name = "users/info.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # 사용자가 요청한 userid 가져오기
        userid = self.request.GET.get("id")

        # user 찾기
        suser= get_object_or_404(CustomUser, pk=userid)
        context['suser'] = suser

        # 가져온 userid를 이용해서 사용자가 작성한 게시물 가져오기
        contents = Content.objects.select_related('user').prefetch_related('image_set').filter(user=suser)
        context['contents'] = contents

        # 팔로우
        follower = FollowRelation.objects.filter(followee=suser).count()
        context['follower'] = follower

        try:
            # 로그인 사용자의 팔로우 목록을 추출
            cur_followers = FollowRelation.objects.get(follower=self.request.user).followee.all()
            context['followees_ids'] = list(cur_followers.values_list('id', flat=True))
        except FollowRelation.DoesNotExist:
            context['followees_ids'] = 0


        try:
            # 검색한 사용자의 팔로우 수 추출
            followers = FollowRelation.objects.get(follower=suser).followee.count()
            context['followees'] = followers
        except FollowRelation.DoesNotExist:
            context['followees'] = 0


        return context




# 기존방식 - 지금은 사용하지 않음
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