
from django.contrib import admin
from django.urls import path
from myapp.views import create_article_view,get_subject_from_wikipedia_view

urlpatterns = [
    path("create-article/", create_article_view, name='create_article'),
    path("get-subject-from-wiki/",get_subject_from_wikipedia_view, name="get_subject_from_wikipedia_view" )
]
