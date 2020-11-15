from django.conf import settings
from django.db import models
from django.urls import reverse

class Announcement(models.Model):
    title = models.CharField(max_length=255)
    bodyText = models.TextField()
    COLORS = (("", "None"),
              ("bg-primary", "Primary"),
              ("bg-secondary", "Secondary"),
              ("bg-success", "Success"),
              ("bg-info", "Info"),
              ("bg-warning", "Warning"),
              ("bg-danger", "Danger"),
              ("bg-light", "Light"),
              ("bg-dark", "Dark")
             )
    color = models.CharField(max_length=15, choices=COLORS, blank=True, default="")
    topic = models.ForeignKey('Topics', on_delete=models.CASCADE)
    relatedCourseNumber = models.ForeignKey('CourseNumber', on_delete = models.CASCADE, blank=True, default=2)
    entryDate = models.DateField(auto_now_add=True)
    startDate = models.DateField(null=False)
    expirationDate = models.DateField(null=False)
    modificationDate = models.DateField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title[:50]

    def get_absolute_url(self):
        return reverse("announcementDetail", args=[str(self.id)])

class Topics(models.Model):
    topicName = models.TextField(max_length=50, unique=True)
    topicComments = models.CharField(max_length=200, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.topicName

    # def get_absolute_url(self):
    #     return reverse('topicList')

class CourseNumber(models.Model):
    DISCIPLINES = (("XX", "None"),
                    ("AC", "Accounting"),
                    ("AR", "Art"),
                    ("CO", "Communication"),
                    ("CS", "Computer Science"),
                    ("CJ", "Criminal Justice"),
                    ("CU", "Culinary Arts"),
                    ("EN", "English"),
                    ("FS", "Food/Resturant Service Mgmt"),
                    ("GD", "Graphic Design"),
                    ("HA", "Health Care Mgmt"),
                    ("HO", "Honors"),
                    ("HR", "Hotel/Resort Mgmt"),
                    ("HU", "Humanities"),
                    ("ID", "Interior Design"),
                    ("MN", "Management"),
                    ("MK", "Marketing"),
                    ("MH", "Mathematics"),
                    ("PM", "PM"),
                    ("LW", "Pre-Law"),
                    ("PS", "Psychology"),
                    ("SC", "Science"),
                    ("SS", "Social Science"),
                    ("SM", "Sports Management"),
                    ("HR", "Human Resource Mgmt."))

    fullCourseNumber = models.CharField(max_length=10, unique=True)
    discipline = models.CharField(max_length=50, unique=True, choices=DISCIPLINES)
    courseTitle = models.CharField(max_length=200)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.fullCourseNumber

    # def get_absolute_url(self):
    #     return reverse('courseNumberList')

