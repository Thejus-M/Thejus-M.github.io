"""Thejus_M URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
    
"""
from django.contrib import admin
from .settings import DEBUG,MEDIA_URL,MEDIA_ROOT
from django.urls import include, path
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('home.urls')),
]

if DEBUG:
    urlpatterns += static(MEDIA_URL,
                        document_root=MEDIA_ROOT)
