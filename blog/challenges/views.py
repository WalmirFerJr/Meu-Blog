from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

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