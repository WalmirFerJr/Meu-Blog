from django.urls import path
from . import views # importando arquivo views da mesma pasta em que nosso arquivo atual esta

urlpatterns = [
 path("<month>", views.monthlyPost) # <> para utilizar placeholders e criar caminhos dinâmicos
]

