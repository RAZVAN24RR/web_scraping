from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from myapp.services.article_service import create_article

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

# Create your views here.
