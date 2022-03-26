from django.http import HttpResponse
from django.shortcuts import render
# from  django101.tasks.models import Task

# Create your views here.
#
# def home(request):
#     return  HttpResponse("It works")

def my_view(request):
    return HttpResponse('ole')

def home(request):
    return  render(request,'index.html')