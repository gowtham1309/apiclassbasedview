from django.shortcuts import render

# Create your views here.
from app1.serializers import *
from rest_framework.response import Response
from app1.models import *

from rest_framework.views import APIView
class productcurd(APIView):
    def get(self,request):
        PQS=product.objects.all()
        PJD=productSerializer(PQS,many=True)
        return Response(PJD.data)
    def post(self,request):
        pass

    