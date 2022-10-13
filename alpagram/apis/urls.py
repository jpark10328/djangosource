from django.urls import path
from . import views

urlpatterns = [
    path("v1/users/create/", views.UserCreateView.as_view(), name="apis_v1_users_create"),
]
