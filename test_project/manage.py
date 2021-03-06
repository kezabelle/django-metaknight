from __future__ import unicode_literals
from __future__ import absolute_import
import os
import sys
from django import VERSION as django_version
from django.conf.urls import url, include

# this module
me = os.path.splitext(os.path.split(__file__)[1])[0]
# helper function to locate this dir
def here(*args):
    return os.path.abspath(
        os.path.join(os.path.abspath(os.path.dirname(__file__)), *args))

sys.path.append(here('..'))

# SETTINGS
DEBUG = True
TEMPLATE_DEBUG = True
ROOT_URLCONF = me
DATABASES = {'default': {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': here('db.sqlite3'),
}}
TEMPLATE_DIRS = (here('templates'), )
SECRET_KEY = '$2274f6b78ef89ea2d67e067f498b5a0241c7874c$'
SITE_ID = 1


INSTALLED_APPS = [
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.staticfiles",
    "django.contrib.sitemaps",
    "django.contrib.messages",
    "django.contrib.admin",

    "taggit",
    # "robots",
    "treebeard",
    "debug_toolbar",
    'rest_framework',

    "varlet",
    "editregions",
    "churlish",
    "menuhin",
    "adminlinks",
    "moreloaders",
    "patternatlas",
]

if django_version[:3] >= (1, 7, 0):
    debugger_needed_at = 0
else:
    debugger_needed_at = INSTALLED_APPS.index('django.contrib.admin') + 1
INSTALLED_APPS.insert(debugger_needed_at, "werkzeug_debugger_runserver")


STATIC_URL = '/s/'
MEDIA_URL = '/m/'
# TEMPLATE_LOADERS = (
#     ('moreloaders.mostlycached.Loader', (
#         'django.template.loaders.filesystem.Loader',
#         'django.template.loaders.app_directories.Loader',
#     )),
# )
MOSTLYCACHED_EXCLUDES = (
    r'^.+\.json$',
)

MIDDLEWARE_CLASSES = (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
 )

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
)


class DoItLazy(object):
    def __iter__(self):
        from django.contrib import admin
        admin.autodiscover()
        yield url(r'^admin/', include(admin.site.urls))

        from patternatlas import urlconf as styleguide_urls
        yield url(r'^styleguide/', styleguide_urls)

        from metaknight.drf import v1_router
        yield url(r'^api/v1/', include(v1_router.urls))

        from varlet import named_urls as page_urls
        yield url(r'^', page_urls)
        yield url(r'^robots\.txt$', include('robots.urls'))

        from django.contrib.sitemaps.views import sitemap
        from varlet.sitemaps import PageSitemap
        from patternatlas.sitemaps import PatternSitemap
        yield url(r'^sitemap\.xml$', sitemap, {'sitemaps': {
            'pages': PageSitemap,
            'styleguide': PatternSitemap,
        }})

    def __reversed__(self):
        return reversed(tuple(iter(self)))

    def __radd__(self, other):
        return other + list(iter(self))

    def __add__(self, other):
        return list(iter(self)) + other


urlpatterns = DoItLazy()

if __name__ == '__main__':
    os.environ['DJANGO_SETTINGS_MODULE'] = me
    sys.path += (here('.'),)
    # lazy_config()
    # run the development server
    from django.core import management
    management.execute_from_command_line()
