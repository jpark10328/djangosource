from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from users.forms import RegisterForm
from django.contrib.auth import authenticate,login
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from users.models import Profile

class BaseView(View):
    """
    요청에 대해서 JsonResponse로 응답하는 View
    """
    @staticmethod
    def response(result={}, status=200):

        # key,value
        return JsonResponse(result, status=status)

@method_decorator(login_required, name="dispatch")
class ProfileUpdateView(BaseView):
    def post(self, request):
        """
        file 만 하나 가져오기
        """
        image = request.FILES['file']
        print(image.name)
        print("*"*10)

        profile = Profile.objects.get(user=request.user)
        profile.image = image
        # profile.image = "profile/"+image.name
        profile.save()

        return self.response({"error":False, "message":"success"})





@method_decorator(login_required, name="dispatch")
class ProfileDeleteView(BaseView):

    def get(self, request):
        """
        현재 사용자의 Profile 찾은 후 현재 사진을 default.png 로 변경
        """
        profile = Profile.objects.get(user=request.user)
        print(profile.image.url) # /media/profile/profile.jpg

        # /media/profile/profile.jpg ==> /media/profile/default.jpg
        # 테이블 상에서는 /media/ 는 디폴트 값이므로 profile/default.jpg 로 경로지정
        pos = profile.image.url.rfind("/")
        img_url = profile.image.url[7:pos] # profile

        profile.image = img_url + "/default.png"
        profile.save()

        return self.response({"error":False, "message":"success"})

class UserCreateView(BaseView):
    """
    사용자 생성
    """
    # request 요청이 들어왔을 때 get or post 냐 분별
    def dispatch(self, request, *args, **kwargs):
        return super(UserCreateView, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # 비밀번호 따로 저장
            user.set_password(form.cleaned_data['password'])
            user.save()

            # 로그인 처리
            login_user = authenticate(username = form.cleaned_data['email'], password=form.cleaned_data['password'])
            login(request, login_user)

            return self.response({"error":False, 'message':"success"})
        else:
            # email 중복,값이 없을 때
            return self.response({"error":True, "message":form.errors}, status=400)
