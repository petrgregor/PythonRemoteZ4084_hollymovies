from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    return HttpResponse("Hello World!")


def hello2(request, s):
    return HttpResponse(f"Hello, {s} World!")


def hello3(request):
    s = request.GET.get('s', '')
    return HttpResponse(f"Hello, {s} World!")


def hello4(request, s):
    t = request.GET.get('t', '')
    return HttpResponse(f"Your words: {s}, {t}")


def add(request, num1, num2):
    return HttpResponse(f"{num1} + {num2} = {num1+num2}")

# Domácí úkol:
# Napsat funkci add2, která bude sčítat,
# ale parametry bude načítat pomocí kódování URL
# Např.: http://127.0.0.1:8000/add2?num1=2&num2=3
