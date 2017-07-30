from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.template.loader import get_template
# Create your views here.
def response_hello_world(request):
    return HttpResponse('Hello, World!')

def render_index(request):
    index_template = get_template('index.html')
    posts = Post.objects.all()
    index = index_template.render(locals())
    return HttpResponse(index)
