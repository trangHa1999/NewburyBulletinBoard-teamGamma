from django.contrib import admin
from .models import Article, ClassSchedule, Semester, CourseTopic

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('vetted', 'current', 'title', 'subjectArea', 'subjectAreaSecondary', 'summaryText', 'articleURL', 'image', 'qrcCodeImage', 'entryDate', 'modificationDate', 'author', 'vettedBy', )

    search_fields = ('title', 'subjectArea', 'subjectAreaSecondary', 'current', 'author', 'vetted', 'vettedBy', )

    list_filter = ('title', 'subjectArea', 'subjectAreaSecondary', 'current', 'author', 'vetted', 'vettedBy', )


class ClassScheduleAdmin(admin.ModelAdmin):
    list_display = ('courseNumber', 'semesterName', 'runningInYear', 'runningOnDays', 'roomNumber', 'startTime', 'length', 'subjectArea', 'author',)

    search_fields = ('courseNumber', 'semesterName', 'runningInYear', 'subjectArea', 'roomNumber', 'author',)

    list_filter = ('courseNumber', 'semesterName', 'runningInYear', 'subjectArea', 'roomNumber', 'author',)


class SemesterAdmin(admin.ModelAdmin):
    list_display = ('semesterName', 'semesterYear', 'classSchedules',)

    search_fields = ('semesterName', 'semesterYear', )

    list_filter = ('semesterName', 'semesterYear', )


class CourseTopicAdmin(admin.ModelAdmin):
    list_display = ('courseNumber', 'courseSubjectArea', )

    search_fields = ('courseNumber', 'courseSubjectArea', )

    list_filter = ('courseNumber', 'courseSubjectArea', )


# class CommentInline(admin.StackedInline): model = Comment

admin.site.register(Article, ArticleAdmin)
admin.site.register(ClassSchedule, ClassScheduleAdmin)
admin.site.register(Semester, SemesterAdmin)
admin.site.register(CourseTopic, CourseTopicAdmin)
