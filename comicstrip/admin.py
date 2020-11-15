from django.contrib import admin
from .models import Comic

class ComicAdmin(admin.ModelAdmin):
    list_display = ('vetted', 'current', 'title', 'summaryText', 'image', 'entryDate', 'modificationDate', 'comicAuthor', 'comicVettedBy', )

    search_fields = ('title', 'current', 'comicAuthor', 'vetted', 'comicVettedBy', )

    list_filter = ('title', 'current', 'comicAuthor', 'vetted', 'comicVettedBy', )

admin.site.register(Comic, ComicAdmin)

