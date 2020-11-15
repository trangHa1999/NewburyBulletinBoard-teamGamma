from random import randint

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, ListView
from announcements.models import Announcement
from articles.models import Article, ClassSchedule, CourseTopic
from comicstrip.models import Comic
from datetime import datetime, timedelta, time
from django.db.models import Q
from articles.models import selectSemester
from pytz import timezone

def getRunningClass(dateNTime, searchSemester, searchYear, searchRoomNumber):
    dayCodeMapping = ['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su']
    weekDayName = dateNTime.weekday()  # Weekday begins on Monday; value = 0
    hourNow = dateNTime.hour
    minutesNow = dateNTime.minute
    currentClassCoices = ClassSchedule.objects.filter(runningInYear__exact=searchYear).filter(semesterName__exact=searchSemester).filter(roomNumber__exact=searchRoomNumber, runningOnDays__contains=dayCodeMapping[weekDayName])
    for possibleClass in currentClassCoices:
        classEndTime = datetime.combine(datetime.now(), possibleClass.startTime) + timedelta(hours=possibleClass.length.hour, minutes=possibleClass.length.minute)
        if possibleClass.startTime.hour <= hourNow and classEndTime.hour >= hourNow:
            if classEndTime.hour == hourNow and classEndTime.minute >= minutesNow:
                return possibleClass
            else:
                return possibleClass
    return None


def announcementsAndArticles(request):
    todaysDate = datetime.now()
    selectedRoomNumber = "AC008"

    announcements = Announcement.objects.order_by("-startDate").filter(startDate__lte=todaysDate).filter(expirationDate__gte=todaysDate)
    announcmentsCount = announcements.count()
    semester, currentYear = selectSemester()
    currentlyRunningClass = getRunningClass(todaysDate, semester, currentYear, selectedRoomNumber)
    topicsList = []
    if currentlyRunningClass:       # Got the class now find the subject(s)
        runningCourseTopics = CourseTopic.objects.filter(courseNumber__exact=currentlyRunningClass.courseNumber)
        for topic in runningCourseTopics:
            topicsList.append(topic.courseSubjectArea)

    if len(topicsList) > 1:         # Found topics for the current course.
        scheduledArticles = Article.objects.filter(vetted__exact=True).filter(current__exact=True).filter(Q(subjectArea=topicsList[0]) | Q(subjectAreaSecondary=topicsList[1])).order_by("-entryDate")
    elif len(topicsList) == 1:  # Found topics for the current course.
        scheduledArticles = Article.objects.filter(vetted__exact=True).filter(current__exact=True).filter(
            Q(subjectArea=topicsList[0]) | Q(subjectAreaSecondary=topicsList[0])).order_by("-entryDate")
    else:
        scheduledArticles = Article.objects.filter(vetted__exact=True).filter(current__exact=True).order_by("?")


    generalArticles = Article.objects.filter(vetted__exact=True).filter(current__exact=True).filter(Q(subjectArea="general") | Q(subjectAreaSecondary="general")).order_by("-entryDate")

    comics = Comic.objects.filter(vetted__exact=True).filter(current__exact=True).order_by("-entryDate")[:1]

    return render(request, 'pages/index.html',{'announcements':announcements, 'announcmentsCount':announcmentsCount, 'scheduledArticles':scheduledArticles, 'generalArticles':generalArticles, 'comicStrips':comics})

class HomePageView(ListView):
    model = Announcement
    template_name = "pages/index.html"
    context_object_name = 'announcements'