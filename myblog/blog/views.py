from django.shortcuts import render

from .models import Post

def posts_list(request):
    """
    블로그 글 전체목록
    """
    # 전체목록
    # Post.objects.all()

    # order by
    posts = Post.objects.order_by("-created_at")

    return render(request,"blog/blog_list.html",{"posts":posts})
    
def posts_write(request):
    """
    블로그 작성 - get(글 쓸수 있는 페이지 보여주기), post(글 등록)
    """
    if request.method == "POST":
        pass
    else:
        pass

    return render(request, "blog/post_write.html")