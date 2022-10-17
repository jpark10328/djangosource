from multiprocessing.sharedctypes import Value
from django.db import IntegrityError
from django.http import JsonResponse
from django.views import View
from requests import request
from contents.models import Content, FollowRelation,Image

from users.forms import RegisterForm
from django.contrib.auth import authenticate,login
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from users.models import CustomUser, Profile
from django.db.models import Q

class BaseView(View):
    """
    요청에 대해서 JsonResponse로 응답하는 View
    """
    @staticmethod
    def response(result={}, status=200):

        # key,value
        return JsonResponse(result, status=status)

@method_decorator(login_required, name='dispatch')
class RelationCreateView(BaseView):
    def post(self, request):
        
        try:        
            # id 가져오기
            user_id = request.POST.get('id')
        except ValueError:
            return self.response({"message":"잘못된 요청입니다."},status=400)

        try:
            # id에 해당하는 FollowRelation 가져오기
            relation = FollowRelation.objects.get(follower=request.user)
        except FollowRelation.DoesNotExist:
            relation = FollowRelation.objects.create(follower=request.user)
        
        # 자기자신과 팔로우 하는 것 막기
        try:
            if user_id == request.user:
                raise IntegrityError
        except IntegrityError:
            return self.response({"message":"본인과 팔로우 할 수 없습니다."},status=400)

        # FollowRelation 추가
        relation.followee.add(user_id)
        relation.save()
        return self.response({})


@method_decorator(login_required, name='dispatch')
class RelationDeleteView(BaseView):
    def post(self, request):
        
        try:        
            # id 가져오기
            user_id = request.POST.get('id')
        except ValueError:
            return self.response({"message":"잘못된 요청입니다."},status=400)

        try:
            # id에 해당하는 FollowRelation 가져오기
            relation = FollowRelation.objects.get(follower=request.user)
        except FollowRelation.DoesNotExist:
            return self.response({"message":"잘못된 요청입니다."},status=400)
        
        # 자기자신과 언팔로우 하는 것 막기
        try:
            if user_id == request.user:
                raise IntegrityError
        except IntegrityError:
            return self.response({"message":"본인과 언팔로우 할 수 없습니다."},status=400)

        # FollowRelation이 존재한다면 삭제
        relation.followee.remove(user_id)
        relation.save()
        return self.response({})




@method_decorator(login_required, name='dispatch')
class UserListView(BaseView):
    """
    사용자가 검색어를 입력하면 검색어와 일치하는 user 찾기 : 
    """

    def get(self, request):
        """
        keyword 가져오기, name, nickname 안에 keyword를 가지고 있는 user 찾기
        """
        keyword = request.GET.get('keyword').strip() # request.GET['keyword']

        if keyword:
            user_list = CustomUser.objects.filter(
                Q(name__icontains = keyword)|
                Q(nickname__icontains = keyword)).distinct().select_related('profile')
            
            print(user_list)

            if user_list:
                result = [
                    {
                        "id":user.id,
                        "nickname":user.nickname,
                        "email":user.email,
                        "image":user.profile.image.url

                    } for user in user_list if user != request.user
                ]
                return self.response({"result":result})
            else:
                return self.response({"message":"검색 결과가 없습니다."},status=404)
        else:
            return self.response({"message":"검색어를 확인해 주세요."},status=404)            


@method_decorator(login_required, name='dispatch')
class ContentCreateView(BaseView):
    """
    이미지와 텍스트를 가져와서 입력
    """
    def post(self, request):
        # 텍스트 가져오기
        text = request.POST.get('text').strip()
        content = Content.objects.create(user=request.user, text=text)

        # 이미지 가져오기
        for idx, file in enumerate(request.FILES.values()):
            Image.objects.create(content=content, image=file, order=idx)

        return self.response({})











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
