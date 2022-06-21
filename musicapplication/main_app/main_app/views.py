from django.shortcuts import render
from rest_framework.views import APIView

class HomePage(APIView):
    def get(self,request):
        return render(request,'users/homepage.html')