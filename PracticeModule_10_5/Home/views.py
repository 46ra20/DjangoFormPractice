from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Test(requst):
    return HttpResponse('Hello from Home app')
