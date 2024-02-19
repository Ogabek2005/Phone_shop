from django.urls import path
from .views import *
urlpatterns = [
    path('forma/',FormaListCreateAPIView.as_view()),
]