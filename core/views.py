from django.http import HttpResponse
from django.shortcuts import render, HttpResponse

def hellow(request):
    return HttpResponse("Hellow World")
