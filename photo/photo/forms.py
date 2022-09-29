from django import forms
from .models import Photo

# form 생성 시 forms.Form(일반 폼) or form.ModelForm(모델 폼) 상속받으면서 생성할 수 있음

class PhotoForm(forms.ModelForm):

    # 장고 폼은 내부 클래스로 반드시 Meta 가져야 함
    class Meta:
        # 폼과 연결할 모델
        model = Photo
        # 모델에서 사용할 필드 지정
        fields = ['title','author','image','description','price'] # fields = '__all__' <로 해도됨