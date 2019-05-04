from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('天行健，君子以自强不息')



# Create your views here.
