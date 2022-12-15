from .views import *
from django.urls import path

urlpatterns = [
    path('books', books.as_view()),
    ]
