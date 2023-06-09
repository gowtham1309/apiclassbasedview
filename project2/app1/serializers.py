from rest_framework import serializers
from app1.models import *

class productSerializer(serializers.ModelSerializer):
    class Meta:
        model=product
        fields='__all__'