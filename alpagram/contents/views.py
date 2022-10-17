from django.shortcuts import redirect, render

from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from contents.models import Content, FollowRelation


# def home(request):
#     return render(request, "home.html")

class HomeView(TemplateView):
    template_name = "home.html"

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_anonymous:
            return redirect("contents") 
            
        return super().dispatch(request, *args, **kwargs)


class ContentView(TemplateView):
    template_name = "contents/main.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        # 내용을 추출해서 전송(팔로우 개념 들어가기 전)
        # context["contents"] = Content.objects.filter(user = self.request.user)

        # 내용을 추출해서 전용(로그인 사용자 + 팔로우 사용자)

        # 로그인 사용자 가져오기
        user1 = self.request.user
        
        # 로그인 사용자의 팔로우 목록 가져오기
        # QuerySet [(1,),(2,)] => QuerySet[1,2]
        followees = FollowRelation.objects.filter(follower=user1).values_list('followee__id',flat=True)

        lookup_user_ids = [user1.id] + list(followees)
        context['contents'] = Content.objects.select_related('user').prefetch_related('image_set').filter(user__id__in = lookup_user_ids)


        try:
            followees = FollowRelation.objects.get(follower=user1).followee.all()
            context['followees'] = followees
        except FollowRelation.DoesNotExist:
            context['followees'] = 0

        return context
        


    
    

