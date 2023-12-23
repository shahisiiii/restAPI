from django.shortcuts import render
from serializers import UserRegister
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
# Create your views here.

class Register(APIView):
    def post(self,request,formate=None):
        serializer=UserRegister(data=request.data)
        data={}
        if serializer.is_valid():
            account=serializer.save()
            data['response']='registered'
            data['username']='account.username'
            data['email']=account.email
            token=Token.objects.get(user=account).key
