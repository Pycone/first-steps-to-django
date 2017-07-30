from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^hello-world$', views.response_hello_world),
    url(r'^$', views.render_index),
]