from django.urls import path,include
from . import views

app_name = "app2"

#  File "C:\pythondata\djangosource\template_exam\app2\urls.py", line 6, in <module>
#     path("detail/", admin.site.urls),
# NameError: name 'admin' is not defined

urlpatterns = [   
    path('detail/', views.detail, name="detail"),   
]
