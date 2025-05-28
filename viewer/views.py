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
# Např.:
# http://127.0.0.1:8000/add2?num1=2&num2=3 -> 2 + 3 = 5
# http://127.0.0.1:8000/add2               -> 0 + 0 = 0
# http://127.0.0.1:8000/add2?num1=2        -> 2 + 0 = 2
# http://127.0.0.1:8000/add2?num2=3        -> 0 + 3 = 3
# http://127.0.0.1:8000/add2?num2=2&num1=3 -> 3 + 2 = 5
def add2(request):
    num1 = int(request.GET.get('num1', 0))
    num2 = int(request.GET.get('num2', 0))
    return HttpResponse(f"{num1} + {num2} = {num1+num2}")
