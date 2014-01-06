from django.contrib import admin

from .models import Photo


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('photo', 'title', 'description', 'priority', 'on_home')
    list_editable = ('title', 'description', 'priority', 'on_home')
admin.site.register(Photo, PhotoAdmin)
