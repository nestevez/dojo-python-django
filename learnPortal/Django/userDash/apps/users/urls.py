from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^new/', views.new_user, name='new_user'),
    url(r'^edit/$', views.edit_prof, name='edit_prof'),
    url(r'^message/', views.msg, name='sendmsg'),
    url(r'^show/(?P<user_id>\d+)/', views.wall, name='user_info'),
    url(r'^edit/(?P<user_id>\d+)/', views.edit_user, name='edit_user'),
    # url(r'^delete/(?P<user_id>\d+)/', views.delete, name='delete'),
]
