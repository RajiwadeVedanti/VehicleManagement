from django.shortcuts import render
from django.http import HttpResponse

def get_vehicle(request):
    return HttpResponse("hello world")