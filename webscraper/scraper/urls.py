from django.urls import path
from .views import scrape_wikipedia

urlpatterns = [
    # Definim o rută care să accepte parametrul `text` direct din URL
    path('scrape/<str:query>/', scrape_wikipedia, name='scrape_wikipedia'),
]