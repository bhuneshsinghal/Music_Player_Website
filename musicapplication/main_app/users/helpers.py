from pyexpat.errors import messages
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import redirect
from users.models import CustomUser

def send_verify_email(user,auth_token):
    subject = "Your Music Boss Account needs verification."
    message = "Hi, {} please click on this link to verify your account. http://100.24.20.241/:8000/user/success/{}".format(user.email,auth_token)
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [user.email]
    send_mail( subject, message, email_from, recipient_list )
    
def verify_token(auth_token):
    try:
        user = CustomUser.objects.filter(auth_token=auth_token).first()
        if user:
            user.is_verified = True
            user.save()
    except Exception as e:
        print(e)
