from django.conf.urls import patterns, include, url
from django.views import generic

from .models import Photo


urlpatterns = patterns('',
    url(r'^$', generic.ListView.as_view(queryset=Photo.objects.filter(on_home=False)), name='cms_photo_list')
)
