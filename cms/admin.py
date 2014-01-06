from django.contrib import admin

from .models import Photo


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('photo', 'title', 'description', 'priority')
    list_editable = ('title', 'description', 'priority')
admin.site.register(Photo, PhotoAdmin)
