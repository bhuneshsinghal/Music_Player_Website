from logging import exception
import uuid
from rest_framework.views import APIView
from .models import CustomUser
from .serializers import UserSerializer,RegisterSerializer
from rest_framework.response import Response
from django.contrib.auth import authenticate,login,logout
from rest_framework import status
from django.shortcuts import redirect, render
from django.contrib import messages
from users.helpers import send_mail,send_verify_email
# Create your views here.

def success(request):
    return render(request, 'users/success.html')

def error(request):
    return render(request,"users/error.html")

def verify(request):
    return render(request,"users/token_send.html")

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
        try:
            if CustomUser.objects.filter(email=email).first():
                user = authenticate(email=email,password=password)
                if user.is_verified:
                    login(request,user)
                    return redirect("user/success/")
                else:
                    return redirect("user/login/")
        except Exception as e:
            print(e)

class logoutUser(APIView):
    def get(self,request,*args,**kwargs):
        user = request.user.email
        if user is not None:
            logout(request)
            return render(request,'users/logout.html')



class RegisterUser(APIView):
    def get(self,request,*args,**kwargs):
        return render(request,'users/signup.html')

    def post(self,request,*args,**kwargs):
        user_data = request.POST 
        try:
            email = user_data.get('email')
            if CustomUser.objects.filter(email=email).first():
                messages.success(request,"Given email id is already in use")
                return redirect('/user/register')
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
                    user.auth_token = str(uuid.uuid4())
                    user.save()
                    send_verify_email(user,user.auth_token)
                    return redirect("/user/verify/")
                
                else:
                    messages.success(request,"Given passwords are not matching.")
                    return redirect("/user/register/")
            else:
                messages.success(request,"Please provide details before clicking signup")
                return redirect("/user/register/")
        except Exception as e:
            print(e)

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





        