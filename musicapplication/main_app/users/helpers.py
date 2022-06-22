from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import redirect
from users.models import CustomUser

def send_verify_email(user,auth_token):
    subject = "Your Music Boss Account needs verification."
    message = "Hi, {} please click on this link to verify your account. http://127.0.0.1:8000/user/verify/{}".format(user.email,auth_token)
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [user.email, ]
    send_mail( subject, message, email_from, recipient_list )
    
def verify(auth_token):
    try:
        user = CustomUser.objects.filter(auth_token=auth_token).first()
        if user:
            user.is_verified = True
            user.save()
            return redirect('/user/login')
        else:
            return redirect()
    except Exception as e:
        print(e)
