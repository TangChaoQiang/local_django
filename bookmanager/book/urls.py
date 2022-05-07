from django.urls import path
from book.views import index, hello

urlpatterns = [
    path('index/', index),
    path('hello/', hello)
]