from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index2(request):
    return HttpResponse("Hello, world This is andy. You're at the polls index.")
def index(request):
    return HttpResponse("Hello, world This is andy. You're at the polls index.")