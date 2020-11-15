"""mb_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from . import views
from users.views import SignUp, Profile, activate, resend, EditProfile

urlpatterns = [
    path('signup/', SignUp.as_view(), name="signup"),
    path('profile/', Profile.as_view(), name="profile"),
    path('activate/<key>', activate, name="activateUser"),
    path('resend/<userId>', resend, name="resend"),
    path('profile/edit/', EditProfile.as_view(), name="setting")

]
