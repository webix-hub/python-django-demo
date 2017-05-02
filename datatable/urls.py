from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^data(/|)((?P<id>[0-9]+)|)$', views.data)
]