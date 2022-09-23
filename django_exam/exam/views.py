from django.shortcuts import render, redirect
from .forms import NameForm, MusicianForm


# HttpResponse : 응답 객체
    # 1) 문자열을 담아서 리턴
    # 2) 특정 페이지를 리턴
    #   return HttpResponse(template.render(탬플릿, 전달해줄 객체))


#함수형 뷰
def index(request):
    return render(request, "index.html")

def custom_form(request):
    """
    forms 를 이용하지 않는 방식
    """
    if request.method == "POST":
        # name 가져오기
        # 프린트
        name = request.POST['name']
        print(name)
        # 이름이 홍길동이 아닌 경우
        if name != '홍길동' :
            return redirect("custom_form")
        else:
            return redirect("index")
    return render(request, "custom_form.html")


def django_form(request):
    """
    is_valid() : 유효성 검증
                name = forms.CharField(max_length=20)
                not null, max_length=20 검증

    is_valid() 통과 시 cleaned_data 딕셔너리에 값을 담아 줌
    """
    if request.method == "POST":
        # name 값 가져오기
        form = NameForm(request.POST)
        if form.is_valid():

            return redirect("index")
    else:
        form = NameForm()

    return render(request, "django_form.html", {"form":form})


def musician_create(request):
    """
    musician 추가
    """


    if request.method == 'POST':
        form = MusicianForm(request.POST)
        if form.is_valid():
            # 저장
            form.save() # 모델폼을 상속받은 상태이기 때문에 가능
            return redirect('index')

    else:
        form = MusicianForm()
    return render(request, "musician_register.html", {"form":form})