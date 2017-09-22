from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name='user_dashboard'),
    url(r'^admin/', views.admin, name='admin_dashboard'),
]
