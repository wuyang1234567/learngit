from django.shortcuts import render

# Create your views here.
def list(request):
    return render(request,"article/list.html")
def details(request):
    return render(request,"article/details.html")
def write(request):
    return render(request,"article/write.html")