from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.display),
    url(r'^submit/reg/', views.subreg),
    url(r'^submit/log/', views.sublog),
    url(r'^users/', views.users),
]
