from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.http import require_GET, require_POST


@require_GET
def hello_devops(request):
    return HttpResponse("Hello, DevOps!")


@require_GET
def health_check(request):
    """
    Perform a health check and return a JSON response.
    """
    status = "OK"
    data = {"status": status}
    return JsonResponse(data)
