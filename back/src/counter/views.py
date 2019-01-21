from django.shortcuts import render
from django.http import JsonResponse

def history(request):
    history = {
        'chiffre1' : 1,
        'action' : '+',
        'chiffre2' : 1,
        'results' : 2
    }
    return JsonResponse(history)