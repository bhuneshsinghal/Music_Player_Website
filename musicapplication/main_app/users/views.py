from django.shortcuts import render
from rest_framework.views import APIView
from .models import CustomUser
from .serializers import UserSerializer
from rest_framework.response import Response
# Create your views here.
class UserView(APIView):

    def get(self, request, pk = None ,format=None):
        if pk==None:
            users = CustomUser.objects.all()
            serializer = UserSerializer(users,many=True)
            return Response(serializer.data)
        else:
            user = CustomUser.objects.get(id=pk)
            serializer = UserSerializer(user)
            return Response(serializer.data)

        