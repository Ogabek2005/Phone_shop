from django.shortcuts import render

from .serializer import FormaSerializer
from rest_framework.views import APIView
# Create your views here.
from Phone.models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.serializers import ModelSerializer
from rest_framework.generics import *

class FormaListCreateAPIView(ListCreateAPIView):
    queryset = Forma.objects.all()
    serializer_class = FormaSerializer