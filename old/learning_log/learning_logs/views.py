from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")


def angela(request):
    return render(request,"Page2.html")
def cato(request):
    return render(request,"cats.html")