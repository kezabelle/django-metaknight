from __future__ import unicode_literals
from __future__ import absolute_import
import os
import sys
from django.conf.urls import url, include

# this module
me = os.path.splitext(os.path.split(__file__)[1])[0]
# helper function to locate this dir
here = lambda x: os.path.join(os.path.abspath(os.path.dirname(__file__)), x)

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
INSTALLED_APPS = (
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.staticfiles",
    "django.contrib.sitemaps",
    "django.contrib.messages",
    "django.contrib.admin",
    "werkzeug_debugger_runserver",
    "taggit",
    "robots",
    "treebeard",
    "debug_toolbar",

    "varlet",
    "editregions",
    "churlish",
    "menuhin",
    "adminlinks",
    "moreloaders",
    "patternatlas",
)
STATIC_URL = '/s/'
MEDIA_URL = '/m/'
TEMPLATE_LOADERS = (
    ('moreloaders.mostlycached.Loader', (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )),
)
MOSTLYCACHED_EXCLUDES = (
    r'^.+\.json$',
)


class DoItLazy(object):
    def __iter__(self):
        from django.contrib import admin
        from django.contrib.sitemaps.views import sitemap
        from varlet import named_urls as page_urls
        from patternatlas import urlconf as styleguide_urls
        admin.autodiscover()
        yield url(r'^admin/', include(admin.site.urls))
        yield url(r'^styleguide/', styleguide_urls)
        yield url(r'^', page_urls)
        yield url(r'^robots\.txt$', include('robots.urls'))

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
