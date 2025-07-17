from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def get_question(request):
    data = {
        "id": 1,
        "text": "ประเทศไทยมีกี่จังหวัด",
        "choices": [50, 68, 72, 77]
    }
    return JsonResponse(data, json_dumps_params={'ensure_ascii': False})


@csrf_exempt
def create_question(request):
    if request.method == 'POST':
        try:
            body = json.loads(request.body)
            data = {
                "id": 9,
                "text": body.get("text"),
                "choices": body.get("choices")
            }
            return JsonResponse(data, status=201, json_dumps_params={'ensure_ascii': False})
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
    return JsonResponse({"error": "Method not allowed"}, status=405)









