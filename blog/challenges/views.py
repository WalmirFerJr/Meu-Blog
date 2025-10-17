from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

def monthlyNumber(request, month):
    if month <= 12 and month > 0:
        return HttpResponse(month)
    else:
        return HttpResponseNotFound("O ano tem apenas 12 mêses")

def monthlyPost(request, month): # o argumento month será utilizado como placeholder em urls 
    
    post_text = None
    
    if month == "january":
        post_text = 'Em Janeiro...'
    elif month == "february":
        post_text = 'Em Fevereiro...'
    elif month == "september":
        post_text = 'Em setembro...'
    else:
        return HttpResponseNotFound("Esse Mês não está incluso")
    return HttpResponse(post_text)