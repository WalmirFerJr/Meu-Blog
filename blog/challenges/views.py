from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

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
monthly_keys = list(monthly_post.keys())

# Create your views here.

def monthly_number(request, month):
    if month > len(monthly_keys):
        return HttpResponseNotFound("Este Mês não está incluso")
    else:
        redirect_month = monthly_keys[month - 1]
        redirect_path = reverse("month-challenge", args=[redirect_month])
        return HttpResponseRedirect(redirect_path)     

def monthly_char(request, month): # o argumento month será utilizado como placeholder em urls 
    try:
        post_text = monthly_post[month]
        response_data = f"<h1>{post_text}</h1>" #f-string, indica ao python para avaliar a string seguinte e trata-la de acordo
        return HttpResponse(response_data)
    except:    
        return HttpResponseNotFound("Esse Mês não está incluso")
    
def challenges_page(request):
    page_html = "<ul>"
    
    for month in monthly_keys:
        dynamic_route = reverse("month-challenge", args=[month])
        page_html += f"<li><a href='{dynamic_route}'>{month}</a></li>"
        
    page_html += "</ul>"
    return HttpResponse(page_html)
    