import re
from rest_framework.views import APIView
from .models import CustomUser
from .serializers import UserSerializer,RegisterSerializer
from rest_framework.response import Response
from django.contrib.auth import authenticate,login,logout
from rest_framework import status
from django.shortcuts import render
# Create your views here.
class UserView(APIView):

    def get(self, request, pk = None ,*args,**kwargs):
        if pk==None:
            users = CustomUser.objects.all()
            serializer = UserSerializer(users,many=True)
            return Response(serializer.data)
        else:
            user = CustomUser.objects.get(id=pk)
            serializer = UserSerializer(user)
            return Response(serializer.data)

class LoginUser(APIView):

    def get(self,request,*args,**kwargs):
        return render(request,'users/login.html')

    def post(self,request,*args,**kwargs):
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email,password=password)
        login(request,user)
        return Response("{} successfully logged in".format(user.email))

class logoutUser(APIView):
    def get(self,request,*args,**kwargs):
        user = request.user.email
        if user is not None:
            logout(request)
            return Response("{} has been logged out".format(user))



class RegisterUser(APIView):
    def get(self,request,*args,**kwargs):
        return render(request,'users/signup.html')

    def post(self,request,*args,**kwargs):
        user_data = request.POST
        if user_data.get('password') is not None and user_data.get('confirm_password') is not None:
            
            if user_data.get('password') == user_data.get('confirm_password'):
                
                user = CustomUser.objects.create_user(
                    email = user_data.get('email'),
                    password = user_data.get('password')
                )
                
                if user_data.get('first_name') is not None:
                    user.first_name = user_data.get('first_name')
                
                if user_data.get('last_name') is not None:
                    user.last_name = user_data.get('last_name')
                
                if "date_of_birth" in user_data:
                    user.date_of_birth = user_data.get('date_of_birth')
                
                user.set_password(user_data.get('password'))
                user.save()
                return render(request,'users/login.html')
            
            else:
                return Response({"message":"password is not matching","status":status.HTTP_406_NOT_ACCEPTABLE})
        else:
            return Response({
                "message":"Details are not provided"
            })
        # serializer = RegisterSerializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        # serializer.save(user=request.user)
        # return Response(status=status.HTTP_201_CREATED)

class ChangePassword(APIView):
    def get(self,request,*args,**kwargs):
        return Response(status=status.HTTP_403_FORBIDDEN)
    def post(self,request,*args,**kwargs):
        user1 = authenticate(email=request.data['email'], password=request.data['password'])
        if user1 is not None:
            user1.set_password(request.data['new_password'])
            user1.save()
            return Response({"messgae":"{} your password have been set successfully".format(user1.email)},status=status.HTTP_202_ACCEPTED)
        else:
            return Response({
                "message":"Invalid EmailId or password"

            },status=status.HTTP_401_UNAUTHORIZED)





        