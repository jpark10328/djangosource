from django.urls import path
from . import views

urlpatterns = [
    # User 생성
    path("v1/users/create/", views.UserCreateView.as_view(), name="apis_v1_users_create"),
    # user 검색
    path("v1/users/list/", views.UserListView.as_view(), name="apis_v1_users_list"),


    # 프로필 사진 삭제
    path("v1/users/profile/delete/", views.ProfileDeleteView.as_view(), name="apis_v1_users_profile_delete"),
    # 프로필 사진 업데이트
    path("v1/users/profile/update/", views.ProfileUpdateView.as_view(), name="apis_v1_users_profile_update"),

    # contents 추가
    path("v1/contents/create/", views.ContentCreateView.as_view(), name="apis_v1_content_create"),

    # follow 삭제
    path("v1/relation/delete/", views.RelationDeleteView.as_view(), name="apis_v1_relation_delete"),
    # follow 추가
    path("v1/relation/create/", views.RelationCreateView.as_view(), name="apis_v1_relation_create"),
]
