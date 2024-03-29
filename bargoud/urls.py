from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import autocomplete_light
autocomplete_light.autodiscover()

import views

urlpatterns = patterns('',
    url(r'^autocomplete/', include('autocomplete_light.urls')),
    url(r'^search/', include('haystack.urls')),
    url(r'^photos/', include('cms.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    (r'^api/v2/', include('fiber.rest_api.urls')),
    (r'^admin/fiber/', include('fiber.admin_urls')),
    (r'^jsi18n/$', 'django.views.i18n.javascript_catalog', {'packages': ('fiber',),}),
    (r'', 'fiber.views.page'),
)
