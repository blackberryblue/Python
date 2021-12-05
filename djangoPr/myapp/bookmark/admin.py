from django.contrib import admin

from bookmark.models import Bookmark

# Register your models here.
@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'url')


#amdin stie의 Bookmark와 BookmarkAdmin을 등록하겠다는 뜻
# admin.site.register(Bookmark, BookmarkAdmin)
