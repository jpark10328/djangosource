from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse

from .models import Photo
from .forms import PhotoForm

# HttpResponse : 응답 객체
    # 1) 문자열을 담아서 리턴
    # 2) 특정 페이지를 리턴
    #   return HttpResponse(template.render(탬플릿, 전달해줄 객체))


#함수형 뷰
def home(request):
    return HttpResponse("INDEX")


def photo_list(request):

    # 사진목록 추출한 후 목록을 보내야 함
    # select * from photo_photo; <-sql 실행 코드
    photos = Photo.objects.all()

    return render(request, "photo_list.html",{"photos":photos})
    
def photo_post(request):
    """
    PhotoForm 사용하는 방식
    """

    if request.method == "POST":
        # 사용자 입력값 가져와서 PhotoForm 에 바인딩 시켜 줌
        form = PhotoForm(request.POST)

        if form.is_valid(): # 유효성 검사
            # 입력값 데이터베이스에 저장 (모델 폼인 경우 form.save() 하게 되면 모델에 변화를 주게 됨)
            form.save()

            # 성공 시 리스트 보여주기
            return redirect("photo_list")
    else:
        form = PhotoForm()        

    return render(request, "photo_post2.html", {"form":form})
# def photo_post(request):
#     """
#     PhotoForm 사용하는 방식
#     """

#     if request.method == "POST":
#         #사용자 입력값 가져오기
#         title = request.POST['title']
#         author = request.POST['author']
#         image = request.POST['image']
#         description = request.POST['description']
#         price = request.POST['price']
#         print('사용자 입력값',title,author,image,description,price)
#         #입력값 데이터베이스에 저장
#         photo = Photo(title=title, author=author, image=image, description=description, price=price)
#         photo.save()

#         #성공 시 리스트 보여주기
#         return redirect("photo_list")
#     else:
#         form = PhotoForm()        

#     return render(request, "photo_post2.html", {"form":form})


def photo_detail(request, pk):
    # pk에 해당하는 게시물 가져오기
    #get_object_or_404() : 특정조건에 맞는 레코드가 존재한다면 객체 생성 or 존재하지 않는다면 404
    photo = get_object_or_404(Photo, pk=pk)

    # 템플릿을 보여줄 때 게시물 딸려 보내기
    return render(request, 'photo_detail.html', {"photo":photo})

def photo_remove(request, pk):
    print("삭제",pk)

    # pk에 해당하는 게시물 가져오기
    photo = get_object_or_404(Photo, pk=pk)

    # 찾은 게시물 삭제
    photo.delete()

    # 사진 목록 보기로 이동
    return redirect("photo_list")

def photo_edit(request, pk):

    # pk에 해당하는 게시물 가져오기
    object = get_object_or_404(Photo, pk=pk)


    # post 요청
    if request.method == "POST":
        # 수정 내용 가져오기
        form = PhotoForm(request.POST, instance=object)

        if form.is_valid():
            photo = form.save()
            # 상세보기 이동
            return redirect("photo_detail",pk=photo.pk)
    else:
        # pk에 해당하는 게시물 가져오기
        photo = PhotoForm(instance=object)

    # get 요청
    # 템플릿을 보여줄 때 게시믈 딸려 보내기
    return render(request, 'photo_edit2.html', {"photo":photo})
# def photo_edit(request, pk):

#     # pk에 해당하는 게시물 가져오기
#     photo = get_object_or_404(Photo, pk=pk)


#     # post 요청
#     if request.method == "POST":
#         # 수정 내용 가져오기
#         title = request.POST['title']
#         author = request.POST['author']
#         image = request.POST['image']
#         description = request.POST['description']
#         price = request.POST['price']
#         print('사용자 수정값',title,author,image,description,price)
        
#         # 수정 내용 db 반영하기
#         photo.title = title
#         photo.author = author
#         photo.image = image
#         photo.description = description
#         photo.price = price
#         photo.save()

#         # 상세보기 이동
#         return redirect("photo_detail",pk=photo.pk)

#     # get 요청
#     # 템플릿을 보여줄 때 게시믈 딸려 보내기
#     return render(request, 'photo_edit.html', {"photo":photo})