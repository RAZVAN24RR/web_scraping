from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.shortcuts import get_object_or_404
from myapp.services.article_service import create_article, get_subject_from_wikipedia
from myapp.models import Article
import json
from django.http import JsonResponse
from django.db import connection
import requests



POWER_BI_API_URL = "https://api.powerbi.com/beta/6bb41fe4-40a3-4a10-b6cd-38278e78b21a/datasets/44ad7af8-e468-4704-b899-1f07d10cf1e1/rows?experience=power-bi&key=Cim%2FpvRhvtCyHRpOCFtKDDsmLrvUN52yAL21Ig5K6InXlu2tSIejo6B5be8dZuzyPithZG%2BaNFylt1qORMoNLA%3D%3D"

@csrf_exempt
def create_article_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        title = data.get("title")
        paragraph1 = data.get('paragraph1')
        paragraph2 = data.get('paragraph2')

        if title and paragraph1 and paragraph2:
            create_article(title,paragraph1,paragraph2)
            return JsonResponse({"message": "Article logged and saved successfully!"})
        return JsonResponse({"error": "Missing data in request"}, status=400)
    return JsonResponse({"error": "Invalid method"}, status=405)

@csrf_exempt
def get_subject_from_wikipedia_view(request):
    if request.method == 'POST':
        data = json.loads(request.body);
        subject = data.get("subject")
        
        if(subject):
            get_subject_from_wikipedia(subject)
            return JsonResponse({"message": "Subject received by server"});
        return JsonResponse({"error": "Missing data in request"}, status=400)
    return JsonResponse({"error": "Invalid method"}, status=405)

def get_all_articles_view(request):
    if request.method == 'GET':
        articles = Article.objects.all()

        articles_list = []
        for article in articles:
            articles_list.append({
                "title": article.title,
                "paragraph1": article.paragraph1[:100],
                "paragraph2": article.paragraph2[:100]
            })
        return JsonResponse({"articles": articles_list})
    return JsonResponse({"error": "Invalid request method"}, status=400)

def get_article_by_id_view(request, article_id):
    if request.method == 'GET':
        article = get_object_or_404(Article, id=article_id)
    
        article_data = {
            "title": article.title,
            "paragraph1": article.paragraph1[:200],
            "paragraph2": article.paragraph2[:200],
        }
        return JsonResponse(article_data)
    
    return JsonResponse({"error": "Invalid request method"}, status=405)

@csrf_exempt
def push_data_to_power_bi(request):
    if request.method == 'POST':
        try:
            articles = Article.objects.all()

            articles_list = []
            for article in articles:
                articles_list.append({
                    "title": article.title,
                    "paragraph1": article.paragraph1[:50],  # Limit to 50 characters
                    "paragraph2": article.paragraph2[:50]   # Limit to 50 characters
                })

            json_data = json.dumps(articles_list)

            headers = {
                'Content-Type': 'application/json'
            }

            response = requests.post(POWER_BI_API_URL, headers=headers, data=json_data)

            if response.status_code == 200:
                return JsonResponse({"message": "Data sent successfully!"}, status=200)
            else:
                return JsonResponse({"error": f"Failed to send data. Status code: {response.status_code}"}, status=500)
        
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request method"}, status=405)


