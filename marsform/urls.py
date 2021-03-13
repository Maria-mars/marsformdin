from django.conf.urls import url

import marform.views as views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^done/$', views.done),
    ]