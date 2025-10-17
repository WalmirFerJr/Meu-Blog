from django.urls import path
from . import views # importando arquivo views da mesma pasta em que nosso arquivo atual esta

urlpatterns = [
 path("january", views.januaryView),
 path("february", views.februaryView)
]

