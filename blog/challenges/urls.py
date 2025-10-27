from django.urls import path
from . import views # importando arquivo views da mesma pasta em que nosso arquivo atual esta

urlpatterns = [
 path("<int:month>", views.monthly_number),
 path("<str:month>", views.monthly_char, name="month-challenge"), # <> para utilizar placeholders e criar caminhos dinâmicos str: para tratar o placeholder como uma string
 path("", views.challenges_page)
 
]                                       

