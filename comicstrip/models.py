from django.conf import settings
from django.db import models
from django.urls import reverse

class Comic(models.Model):
    title = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to="comicstrip/images/")
    summaryText = models.TextField(max_length=1023, blank=True)
    current = models.BooleanField(default=True)
    entryDate = models.DateField(auto_now_add=True)
    modificationDate = models.DateField(auto_now=True)
    comicAuthor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comicAuthor', default=1)
    vetted = models.BooleanField(default=False)
    comicVettedBy = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comicVettedBy', default=1)

    def __str__(self):
        return self.title[:50]

    def get_absolute_url(self):
        return reverse("listComics", args=[str(self.id)])

