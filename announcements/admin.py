from django.contrib import admin
from .models import Announcement, Topics, CourseNumber

class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'bodyText', 'topic', 'color', 'relatedCourseNumber', 'entryDate', 'startDate', 'expirationDate', 'modificationDate', 'author',)

    search_fields = ('title', 'topic', 'relatedCourseNumber',)

    list_filter = ('author', 'title', 'topic', 'color', 'relatedCourseNumber', 'modificationDate',)


admin.site.register(Announcement, AnnouncementAdmin)
admin.site.register(Topics)
admin.site.register(CourseNumber)
