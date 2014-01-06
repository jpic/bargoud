from django.conf.urls import patterns, include, url
from django.views import generic

from .models import Photo


urlpatterns = patterns('',
    url(r'^$', generic.ListView.as_view(model=Photo), name='cms_photo_list')
)
