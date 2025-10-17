from django.urls import path
from . import views # importando arquivo views da mesma pasta em que nosso arquivo atual esta

urlpatterns = [
 path("<int:month>", views.monthlyNumber),
 path("<str:month>", views.monthlyPost) # <> para utilizar placeholders e criar caminhos dinâmicos
]                                       # str: para tratar o placeholder como uma string

