from django.urls import path
from . import views # importando arquivo views da mesma pasta em que nosso arquivo atual esta

urlpatterns = [
 path("january", views.januaryView),
 path("february", views.februaryView),
 path("march", views.marchView),
 path("april", views.aprilView),
 path("may", views.mayView),
 path("june", views.juneView),
 path("july", views.julyView),
 path("august", views.augustView),
 path("september", views.septemberView),
 path("october", views.octoberView),
 path("november", views.novemberView),
 path("december", views.decemberView),
]

