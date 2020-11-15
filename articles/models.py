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


QRCIMAGESAVELOCATION = 'articles/images/qrc'
QRCROOTFILENAME = "articlesQRC.svg"

SUBJECTAREAS = (("general", "General"),
                ("programming1", "Programming 1"),
                ("programming2", "Programming 2"),
                ("programming3", "Programming 3"),
                ("programming4", "Programming 4"),
                ("web-client-development", "Web Client Development"),
                ("web-server-development", "Web Server Development"),
                ("web-design", "Web Design"),
                ("databases", "Databases"),
                ("networking1", "Networking 1"),
                ("networking2", "Networking 2"),
                ("security1", "Cyber Security 1"),
                ("security2", "Cyber Security 2"),
                ("linux", "Linux"),
                ("embedded", "Embedded Systems"),
                ("python", "Python"),
                ("c", "C/C++"),
                ("java", "Java"),
                ("javascript", "Javascript"),
                ("php", "PHP"),
                ("servers", "Servers")
                )
SEMESTERS = (("fall", "Fall"),
             ("winter", "Winter"),
             ("spring", "Spring"),
             ("summer1", "Summer 1"),
             ("summer2", "Summer 2"),
             )

YEARS = ((2018, "2018"),
         (2019, "2019"),
         (2020, "2020"),
         (2021, "2021"),
         (2022, "2022"),
         (2023, "2023"),
         (2024, "2024"),
        )

class Article(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="articles/images/", null=True)
    summaryText = models.TextField(max_length=1023, blank=True)
    current = models.BooleanField(default=True)
    subjectArea = models.CharField(max_length=30, choices=SUBJECTAREAS, default=1)
    subjectAreaSecondary = models.CharField(max_length=30, choices=SUBJECTAREAS, blank=True)
    entryDate = models.DateField(auto_now_add=True)
    modificationDate = models.DateField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='author', default=1)
    articleURL = models.URLField(null=False)
    qrcCodeImage = models.ImageField(upload_to="articles/images/qrc/", blank=True)
    vetted = models.BooleanField(default=False)
    vettedBy = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='vettedBy', default=1)

    def __str__(self):
        return self.title[:50]

    def get_absolute_url(self):
        return reverse("article_detail", args=[str(self.id)])

def qrcImageGenerator(urlToEmbed):
    factory = qrcode.image.svg.SvgPathImage
    generatedQRImage = qrcode.make(urlToEmbed, image_factory=factory)
    filename = QRCROOTFILENAME
    generatedQRImage.save(filename)
    return filename

@receiver(pre_save, sender=Article)
def qrcGenCallback(sender, instance, *args, **kwargs):
    instance.qrcCodeImage.mode="SVG"
    filename = qrcImageGenerator(instance.articleURL)
    qrcImageFile = open(filename, 'rb')
    imageData = File(qrcImageFile)
    instance.qrcCodeImage.save(filename, imageData, save=False)


class ClassSchedule(models.Model):
    courseNumber = models.CharField(max_length=10)
    courseTitle = models.CharField(max_length=100, blank=True)
    semesterName = models.TextField(max_length=12, choices=SEMESTERS)
    roomNumber = models.CharField(max_length=8, default="AC008")
    runningInYear = models.IntegerField(default=2018, choices=YEARS)
    startTime = models.TimeField()
    length = models.TimeField(default=85 * 60)
    runningOnDays = models.CharField(max_length=20, default="")
    subjectArea = models.CharField(max_length=30, choices=SUBJECTAREAS, default=1)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return "{0} {1}{2}".format(self.courseNumber, self.semesterName, str(self.runningInYear % 100))

    def get_absolute_url(self):
        return reverse('classScheduleList')


def monthWeekNumber(year, month, day):
    if not isleap(year):
        monthOffset = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    else:
        monthOffset = [0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]
    currentDayOfYear = monthOffset[month - 1] + day
    daysIntoMonth = currentDayOfYear - monthOffset[month - 1]
    weeknumber = (daysIntoMonth // 7) + 1
    return weeknumber

def selectSemester():
    semesterMap = ((("September", "October", "November", "December1"), "fall"),
                   (("December3", "December4", "January1", "January2"), "winter"),
                   (("January3", "January4", "February", "March", "April", "May1"), "spring"),
                   (("May3", "May4", "June1", "June2"), "summer1"),
                   (("June3", "June4", "August1", "August2", "August3", "August4"), "summer2")
                  )

    currentYear = date.today().year
    currentMonth = date.today().month
    currentMonthName = date.today().strftime("%B")
    currentDay = date.today().day

    for monthList, semester in semesterMap:
        for month in monthList:
             if month[-1].isalpha():            # This isn't a split month
                 if currentMonthName == month:
                     return (semester, currentYear)
             else:
                 monthSliceNumber = int(month[-1])
                 monthName = month[:-1]
                 if currentMonthName == monthName:  # Found month, now see if 'slice' matches.
                     weekNumber = monthWeekNumber(currentYear, currentMonth, currentDay)
                     if weekNumber == monthSliceNumber:
                         return (semester, currentYear)
    return ("None", currentYear)        # We are in between semesters :-(

@receiver(pre_save, sender=ClassSchedule)
def setDatedInfoCallback(sender, instance, *args, **kwargs):
    semesterSelection, currentYear = selectSemester()
    instance.semester = semesterSelection
    instance.year = currentYear
    print("Semester: {0} Year: {1}".format(semesterSelection, currentYear))


class Semester(models.Model):
    semesterYear = models.IntegerField(default=2018, choices=YEARS)
    semesterName = models.TextField(max_length=12, choices=SEMESTERS, default="fall")
    classSchedules = models.ForeignKey(ClassSchedule, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return "{0}{1}".format(self.semesterName, str(self.semesterYear % 100))

    def get_absolute_url(self):
        return reverse('semesterList')


def getCurrentClassSchedules(degreePrefix, roomNumber, semester):
    from .nethawkCredentials import loginPayload

    payload2 = {
        'module': 'allUsers',
        'handler': 'public',
        'reset': 'true',
        'mode': '1',
        're': '',
        'startMenuStudentInfo': '',
        'sem': '201910'
    }

    with requests.Session() as nethawkSession:
        """ The first three accesses are for login credentials, agreeing
        to the FERPA agreement and selecting the semester. This code
        accepts the current semester default as created by Nethawk.
        No attempt has been made to allow for specifying the
        semester desired."""

        selectedSemester = "770025738"

        loginPostResults = nethawkSession.post('https://nethawk.newbury.edu/cafeweb/login', data=loginPayload)
        ferpaGetResults = nethawkSession.get('https://nethawk.newbury.edu/cafeweb/Navigation')
        listingGetResults = nethawkSession.get('https://nethawk.newbury.edu/cafeweb/PickSem?mode=1&amp;id={0}'.format(selectedSemester))
        pickSemesterPostResults = nethawkSession.post('https://nethawk.newbury.edu/cafeweb/CourseListing', data=payload2)
        # The listing formed by Nethawk is SERIOUSLY malformed.
        # The table with the course listings is OUTSIDE/AFTER the closing
        # </html> tag. This method extracts that table and wraps it in a
        # simple properly formed html page, to allow Beautiful Soup to
        # be able to parse it.

        htmlTable = fixHtmlCode(pickSemesterPostResults)
        soupBowl = BeautifulSoup(htmlTable, features="lxml")
        tableContent = soupBowl.find('table', {'id':'CourseListingTable'})

        courseListings = []
        for tableRow in tableContent.find_all("tr"):
            if tableRow.th != None:
                headings = []
                headingsList = tableRow.find_all("th")
                for heading in headingsList:
                    headings. append(heading.get_text().strip())

            elif tableRow.td != None:
                courseItems = []
                courseItemsList = tableRow.find_all("td")
                for courseItem in courseItemsList:
                    courseItems.append(courseItem.get_text().replace("CLICK-IT","").replace("CLICK IT", '', 3).strip())
                courseListings.append(courseItems)

        courseListingsList = []
        for counter, course, title, instructor, credits, dayTimeRoom, maxSeats, seatsUsed, seatsLeft, startDate, endDate, department, site, syllabusType, syllabusStartDate, division, crossRegMaxSeats, crossRegSeatsUsed, crossRegSeatsLeft, repeats, comment in courseListings:
            courseString = "{0}\t{1}\t{2}\t{3}\t{4}".format(course, title, instructor, dayTimeRoom, department)
            if course.startswith(degreePrefix):
                courseListingsList.append((course, title.replace('&', ' and ').replace('  ', ' '), instructor, dayTimeRoom, department))
        return courseListingsList


def fixHtmlCode(pickSemesterPostResults):
    htmlInText = pickSemesterPostResults.text.split('\n')
    htmlTable = "<html>\n<head></head>\n<body>\n"
    foundTable = False
    for line in htmlInText:
        if "<table" in line:
            foundTable = True
        elif foundTable and line.count("</table>"):
            htmlTable += line
            foundTable = False
        if foundTable:
            htmlTable += line
    htmlTable += "\n</body>\n"
    return htmlTable


@receiver(pre_save, sender=Semester)
def getNSetClassScheduesCallback(sender, instance, *args, **kwargs):
    semesterSelection = instance.semesterName
    currentYear = instance.semesterYear
    classSchedules = getCurrentClassSchedules("CS", "AC008")

    dayMapping = {'M': 'Mo', 'TU': 'Tu', 'W': 'We', 'TH': 'Th', 'F': 'Fr'}
    for course, title, instructor, dayTimeRoom, department in classSchedules:
        courseNumber, courseSection = course.split('-')
        if courseSection[0] == 'Z':     # Skip Directed Study classes.
            continue
        if len(dayTimeRoom) > 0:
            try:
                if dayTimeRoom.count(' ') == 2:
                    courseDays, courseTimes, roomNumber = dayTimeRoom.split(' ')
                elif dayTimeRoom.count(' ') == 1:
                    courseDays, courseTimes = dayTimeRoom.split(' ')
                    roomNumber = ""
            except ValueError:
                print("Error decomposing dayTimeRoom field")
            courseDays = courseDays.replace(',', ':')
            for originalDayCode, newDayCode in dayMapping.items():
                courseDays = courseDays.replace(originalDayCode, newDayCode)
            courseStartTime, courseEndTimeDelta = courseTimes.split('-')
            courseTimeHour, courseTimeMinutes = courseStartTime[:-1].split(':')
            courseTimeHour = int(courseTimeHour)
            courseTimeMinutes = int(courseTimeMinutes)
            courseStartTimeAmPm = courseStartTime[-1]
            if courseStartTimeAmPm.lower() == 'p' and courseTimeHour != 12: courseTimeHour += 12
            courseStartTimeDelta = timedelta(hours=courseTimeHour, minutes=courseTimeMinutes)
            courseStartTime = time(hour=courseTimeHour, minute=courseTimeMinutes)
            courseTimeHour, courseTimeMinutes = courseEndTimeDelta[:-1].split(':')
            courseTimeHour = int(courseTimeHour)
            courseTimeMinutes = int(courseTimeMinutes)
            courseEndTimeAmPm = courseEndTimeDelta[-1]
            if courseEndTimeAmPm.lower() == 'p' and courseTimeHour != 12: courseTimeHour += 12
            courseEndTimeDelta = timedelta(hours=courseTimeHour, minutes=courseTimeMinutes)
            classLengthDelta = int((courseEndTimeDelta - courseStartTimeDelta).total_seconds() // 60)
            classLength = time(hour=classLengthDelta // 60, minute=classLengthDelta % 60)
            pass
        else:
            courseStartTime = classLength = time(hour=0, minute=0)

        obj, created = ClassSchedule.objects.update_or_create(courseNumber=courseNumber, courseTitle=title.title(), semesterName=semesterSelection, startTime=courseStartTime, length=classLength, roomNumber=roomNumber, runningInYear=currentYear, runningOnDays=courseDays)
        print("{0} {1} {2}{3} {4} {5} {6} {7}".format(courseNumber, title.title(), semesterSelection, currentYear, courseStartTime, classLength, roomNumber, courseDays))


class CourseTopic(models.Model):
    courseNumber = models.CharField(max_length=10)
    courseSubjectArea = models.CharField(max_length=30, choices=SUBJECTAREAS, default=1)

    def __str__(self):
        return "{0} {1}".format(self.courseNumber, self.courseSubjectArea)

    def get_absolute_url(self):
        return reverse('semesterList')


