from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name="form"),
    url(r'^submit_form/', views.submit, name="submit"),
    url(r'^results/', views.results, name="results"),
]
