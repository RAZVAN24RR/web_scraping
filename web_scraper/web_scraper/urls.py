
from django.contrib import admin
from django.urls import path
from myapp.views import create_article_view

urlpatterns = [
    path("create-article/", create_article_view, name='create_article'),
]
