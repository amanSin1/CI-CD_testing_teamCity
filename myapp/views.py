from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

def hello(request):
    return JsonResponse({'message': 'Hello from Django!', 'status': 'success'})

def health(request):
    return JsonResponse({'health': 'OK'})