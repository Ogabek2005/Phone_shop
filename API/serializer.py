from rest_framework.serializers import ModelSerializer , Serializer
from Phone.models import *
from rest_framework.generics import *
from rest_framework import serializers


class FormaSerializer(Serializer):
    full_name = serializers.CharField(max_length=250)
    phone_number = serializers.CharField(max_length=250)


        

    def create(self, validated_data):

        form = Forma.objects.create(
            **validated_data)
        return form
