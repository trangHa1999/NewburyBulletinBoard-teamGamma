from django.conf import settings
from django.db import models
from django.urls import reverse
import qrcode
import qrcode.image.svg
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.files import File
from datetime import date, time, timedelta
from calendar import isleap
import requests
from bs4 import BeautifulSoup

SUBJECTAREAS = (("web-client-development", "Web Client Development"),
                ("web-server-development", "Web Server Development"),
                ("web-design", "Web Design"),
                ("databases", "Databases"),
                ("networking1", "Networking"),
                ("security1", "Cyber Security"),
                ("linux", "Linux"),
                ("embedded", "Embedded Systems"),
                ("python", "Python"),
                ("django", "Django"),
                ("sass", "Sass"),
                ("c", "C/C++"),
                ("java", "Java"),
                ("javascript", "Javascript"),
                ("php", "PHP"),
                ("servers", "Servers")
                )

class Course(models.Model):
    courseTitle = models.CharField(max_length=255)
    subjectArea = models.CharField(max_length=30, choices=SUBJECTAREAS, default=1)
    entryDate = models.DateField(auto_now_add=True)
    modificationDate = models.DateField(auto_now=True)
    articleURL = models.URLField(null=False)

    def __str__(self):
        return self.courseTitle[:50]

    def get_absolute_url(self):
        return reverse("course_detail", args=[str(self.id)])