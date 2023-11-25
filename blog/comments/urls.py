from django.urls import path
from .views import *

urlpatterns = [
    path('', comment_page, name="comment"),
]