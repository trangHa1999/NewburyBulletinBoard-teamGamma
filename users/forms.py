#!/usr/bin/env python
__author__ = "Arana Fireheart"

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.core.mail import send_mail
from random import choice
from string import ascii_letters
from django.utils.timezone import now
from django.utils.dateparse import parse_duration


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ("username", "email", "first_name", "last_name", "age")

@receiver(pre_save, sender=CustomUser)
def setNewUserInactive(sender, instance, **kwargs):
    if instance._state.adding is True:
        activateLink = generateActivationKey(instance)
        instance.is_active = False
        if instance.email.endswith("newbury.edu"):
            result = send_mail('Email confirmation requested', 'Hi {0},\n\nPlease verify your email address by clicking the following link:\n\n{1}\n\nThis link will expire 48 hours after it was generated'.format(instance.username, activateLink), 'admin@newburycs.com',
              [instance.email])
            print("{0} email sent to {1} with link {2}".format(result, instance.email, activateLink))
        else:
            result = send_mail('Account creation denied',
                               'We thank you for your interest in Newbury College and Newbury College Computer Science.\n\nHowever, currently, account creation is for Newbury college students only.\n\nPlease feel free to visit us at any time and read the articles or comicstrips\n\nIf you would like to enroll, please visit <a href="http://www.newbury.edu">http://www.newbury.edu</a>',
                               'admin@newburycs.com',
                               [instance.email])
            print("{0} email sent to {1} without an activation link.".format(result, instance.email))
    else:
        print("Updating User Record")


def generateActivationKey(instance):
    randomString = "".join([choice(ascii_letters) for i in range(0, 64)])
    activateLink = "http://www.newburycs.com/users/activate/{0}".format(randomString)
    instance.activationKey = randomString
    instance.activationExpires = now() + parse_duration("2 days")
    return activateLink


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email", "first_name", "last_name", "age")

