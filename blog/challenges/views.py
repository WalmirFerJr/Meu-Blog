from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def januaryView(request):
    
    return  HttpResponse("Este é o desafio de janeiro!")

def februaryView(request):

    return HttpResponse("Este é o desafio de fevereiro!")