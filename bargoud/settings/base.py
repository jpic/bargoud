import os

from django.conf.global_settings import *

BOWER_INSTALLED_APPS = (
    'jquery',
    'bootswatch',
    'bootstrap',
    'html5shiv',
    'respond',
    'less',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',

    'mptt',
    'easy_thumbnails',
    'fiber',
    'cms',

    'django_extensions',
    'djangobower',
    'south',
    'autocomplete_light',
    'compressor',
    'reversion',
    'yourlabs',
    'bargoud',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'fiber.middleware.ObfuscateEmailAddressMiddleware',
    'fiber.middleware.AdminPageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS += (
    'django.core.context_processors.request',
    'yourlabs.context_processors.expose_settings',
    'cms.context_processors.home_photos',
)

EXPOSE_SETTINGS = ('DEBUG', 'COMPRESS_ENABLED')

PROJECT_ROOT = os.path.join(os.path.dirname(__file__), '..', '..')


def project_directory(*join):
    return os.path.realpath(
        os.path.join(PROJECT_ROOT, *join).replace('\\', '/'))

# {{{ django-compressor stuff
COMPRESS_PRECOMPILERS = (
    ('text/less', 'recess --compile {infile} --compress > {outfile}'),
    ('text/coffeescript', 'coffee --compile --stdio'),
)

COMPRESS_JS_FILTERS = (
    'compressor.filters.jsmin.JSMinFilter',
)

COMPRESS_CSS_FILTERS = (
    'compressor.filters.cssmin.CSSMinFilter',
)
# }}}

# {{{ Internationalization stuff
gettext = lambda s: s
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
TIME_ZONE = 'Europe/Paris'
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'fr'
USE_I18N = True
USE_L10N = True
USE_TZ = True
LANGUAGES = (
    ('en', gettext('English')),
)
# }}}

# {{{ FS and HTTP server static/media configuration
LOCALE_PATHS = (project_directory('locale'),)
MEDIA_ROOT = project_directory('public/media')
MEDIA_URL = '/public/media/'
STATIC_ROOT = project_directory('public/static')
STATIC_URL = '/public/static/'
STATICFILES_DIRS = (project_directory('static'),)
TEMPLATE_DIRS = (project_directory('templates'),)
FIXTURE_DIRS = (project_directory('fixtures'),)
BOWER_COMPONENTS_ROOT = project_directory('static')
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': project_directory('whoosh_index'),
    },
}
# }}}

SITE_ID = 1
SECRET_KEY = '1c1_$nq4y6g&sz=tusc96mt-nuf9mz*d#%#3sy5#&=$o@&gr(h'
ROOT_URLCONF = 'bargoud.urls'
WSGI_APPLICATION = 'bargoud.wsgi.application'
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)
ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'bargoudprod.eu', 'bargoud.yourlabs.org']
