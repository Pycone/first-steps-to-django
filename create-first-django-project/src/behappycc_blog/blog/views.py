from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def response_hello_world(request):
    return HttpResponse('Hello, World!')