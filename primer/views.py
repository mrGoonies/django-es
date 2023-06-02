from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def say_hello(request) -> HttpResponse:
    message: str = 'Hello Pythonista!'

    return HttpResponse(message, content_type='text/plain')
