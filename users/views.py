from django.shortcuts import render

from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm
from django.utils.timezone import now
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, reverse, redirect
from .models import CustomUser
from django.core.mail import send_mail
from .forms import generateActivationKey
from django.contrib.auth.forms import UserChangeForm


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("profile")
    template_name = "users/signup.html"


class Profile(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "users/profile.html"


def activate(request, key):
    activationExpired = False
    alreadyActive = False
    profile = get_object_or_404(CustomUser, activationKey=key)
    if not profile.is_active:
        if now() <= profile.activationExpires:  # Activation successful
            profile.is_active = True
            profile.save()
        else:
            activationExpired = True            # Display: offer user to send a new activation link
            userId = profile.id
    else:                                       # If user is already active, simply display error message
        alreadyActive = True                    # Display : error message
    return render(request, 'users/activation.html', locals())


def resend(request, userId):
    instance = get_object_or_404(CustomUser, id=userId)
    if not instance.is_active:
        activateLink = generateActivationKey(instance)
        result = send_mail('Email confirmation requested', 'Please verify your email address by clicking the following link:\n\n{0}\n\nThis link will expire 48 hours after it was generated'.format(activateLink), 'admin@newburycs.com',
              [instance.email])
        print("{0} email sent to {1} with link {2}".format(result, instance.email, activateLink))
        instance.save()

    return render(request, 'users/resend-result.html', {"email": instance.email})


class EditProfile(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("setting")
    template_name = "users/edit-profile.html"


