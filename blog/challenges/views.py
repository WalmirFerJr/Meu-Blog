from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def januaryView(request): # Cada view deve ter uma função própria
    
    return  HttpResponse("Em janeiro aproveitei um pouco o fim dos vestibulares para tirar férias e fazer uma viagem")

def februaryView(request):

    return HttpResponse("Em Fevereiro estive ansioso em relação ao meu ingresso na USP")

def marchView(request):

    return HttpResponse("Em março...")

def aprilView(request):

    return HttpResponse("Em abril...")

def mayView(request):

    return HttpResponse("Em maio...")

def juneView(request):

    return HttpResponse("Em junho...")

def julyView(request):

    return HttpResponse("Em julho...")

def augustView(request):

    return HttpResponse("Em agosto...")

def septemberView(request):

    return HttpResponse("Em setembro...")

def octoberView(request):

    return HttpResponse("Em outubro...")

def novemberView(request):

    return HttpResponse("Em novembro...")

def decemberView(request):

    return HttpResponse("Em dezembro...")