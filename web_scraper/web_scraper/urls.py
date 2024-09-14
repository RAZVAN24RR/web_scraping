
from django.contrib import admin
from django.urls import path
from myapp.views import create_article_view,get_subject_from_wikipedia_view, get_all_articles_view,get_article_by_id_view, push_data_to_power_bi

urlpatterns = [
    path("create-article/", create_article_view, name='create_article'),
    path("get-subject-from-wiki/",get_subject_from_wikipedia_view, name="get_subject_from_wikipedia_view" ),
    path("get-all-articles/", get_all_articles_view, name="get_all_articlesW"),
    path('get-article-by-id/<int:article_id>/', get_article_by_id_view, name='get_article_by_id'),
    path('send-data-to-power-bi', push_data_to_power_bi, name='send_data_to_power_bi_service'),
]