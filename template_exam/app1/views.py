from django.shortcuts import render

def list(request):
    return render(request, "app1/list.html")


# AttributeError: module 'app1.views' has no attribute 'detail'
def detail(request):
    return render(request, "app1/detail.html")