from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name='home_page'),
    url(r'^signin/', views.signin, name='signin'),
    url(r'^register/', views.register, name='reg'),
    url(r'^valid/signin', views.validreg, name='validreg'),
    url(r'^valid/reg', views.validlog, name='validlog'),
]
