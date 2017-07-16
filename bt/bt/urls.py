"""
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
"""
from django.conf.urls import url, include
from builto import views

urlpatterns = [
    url(r'^$', views.home_page, name='home'),
    url(r'^main/', include('builto.urls')),
    url(r'^chiara/', include('chiara.urls')),
    url(r'^felipe/', include('felipe.urls'))
]
