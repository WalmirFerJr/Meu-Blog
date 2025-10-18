from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

monthly_post = {
    "january": "Em Janeiro...",
    "february": "Em Fevereiro...",
    "march": "Em Março...",
    "april": "Em Abril...",
    "may": "Em Maio...",
    "june": "Em Junho...",
    "july": "Em Julho...",
    "august": "Em Agosto...",
    "september": "Em Setembro...",
    "october": "Em Outubro...",
    "november": "Em Novembro...",
    "december": "Em Dezembro..."
}

# Create your views here.

def monthlyNumber(request, month):
    months = list(monthly_post.keys())
    redirect_month = months[month]
    return HttpResponse(month)
     

def monthlyPost(request, month): # o argumento month será utilizado como placeholder em urls 
    try:
        post_text = monthly_post[month]
        return HttpResponse(post_text)
    except:    
        return HttpResponseNotFound("Esse Mês não está incluso")