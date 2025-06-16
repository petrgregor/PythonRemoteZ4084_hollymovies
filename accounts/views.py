from django.contrib.auth import logout
from django.shortcuts import render, redirect


def user_logout(request):
    logout(request)
    return redirect(request.META.get('HTTP_REFERER', '/'))  # zůstat na stejné stránce
