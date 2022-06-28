"""main_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from users import views
from . import views as mainview
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views as v
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',mainview.HomePage.as_view(),name='homepage'),
    path('user/view/', views.UserView.as_view() , name="user_view"),
    path('user/view/<int:pk>/', views.UserView.as_view() , name="user_view_with_pk"),
    path('user/register/',views.RegisterUser.as_view(),name="user_registration"),
    path('user/change_password/',views.ChangePassword.as_view(),name='change_password'),
    path('user/login/',views.LoginUser.as_view(),name='user_login'),
    path('user/logout/',views.logoutUser.as_view(),name='user_logout'),
    path('user/success/<auth_token>',views.success,name="success"),
    path('user/verify/',views.verify,name="verify"),
    path('user/error',views.error,name="error"),
    path('api-token-auth/',v.obtain_auth_token,name="token_generate_url"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
