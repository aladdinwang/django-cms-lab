# -*- coding: utf-8 -*-
import os
gettext = lambda s: s
PROJECT_PATH = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]

print PROJECT_PATH

DEFAULT_IMAGE_ASY_FILE = 'generate_png.asy'

# Django settings for cms project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG


ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'db_djangocmslab',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': '127.0.0.1',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '5432',                      # Set to empty string for default.
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'zh'

LANGUAGES = [
    ( 'zh-cn', 'Simplified Chinese' ),
]

"""
CMS_LANGUAGES = {
    1: [{
        'code': 'zh-cn',
        'name': gettext('Simplified Chinese'),
        'public': True,
        'hide_untranslated': True,
        'fallbacks': ['en', ],
    },
    {
    'code': 'en',
    'name': gettext('English'),
    'public': True,
    'hide_untranslated': True,
    },
    ]
}

"""


SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = os.path.join( PROJECT_PATH, "media" )
DEFAULT_IMAGE_PATH =  "default/images"

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = os.path.join( PROJECT_PATH, "static_bak" )
#STATIC_ROOT = '/home/aladdin/jiapin/cmslab/static/'
# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join( PROJECT_PATH, "static" ),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'guhfwxv3453mym=p$lipk4gchhr)c4g3(dj&$0eqk4=k((a!z='

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'cms.context_processors.media',
    'sekizai.context_processors.sekizai',
)


MIDDLEWARE_CLASSES = (
    #'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',

    
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'cmslab.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'cmslab.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join( PROJECT_PATH, "templates" ),
    os.path.join( PROJECT_PATH, 'media/templates' ),
)

CMS_TEMPLATES = (
    ('template_1.html', 'Template One'),
    ('template_2.html', 'Template Two'),
    ( 'news_template.html', 'News Template' ),
    ( 'imageurl.html', 'Image Url' ),
    ('photography.html', 'Photography'),
)

# the relative path to template dir is
# CMS_BASE_TEMPLATE_PREFIX + base_template_path
CMS_BASE_TEMPLATE_PREFIX = 'base/'

CMS_BASE_TEMPLATES = (
    ('photography.html', 'Photography'),
    ('notexist.html', 'NotExist'),
)

CMS_WEBAPPS = (
    ('/home/aladdin/jiapin/demo/templates/master/', 'demo'),
)

CMS_PLACEHOLDER_CONF = {
    'jiapin_img' : {
        'plugins': ['PicturePlugin'],
        'name':gettext("Img"),
        'limits': {
            'global': 1,
         },
     },
    'group image' : {
        'plugins' : ['PicturePlugin'],
        'name': gettext('Imgage'),
        'limits': {
            'global': 1,
         },
     },
    'group text' : {
        'plugins' : ['TextPlugin'],
        'name': gettext('Text'),
        'limits': {
            'global': 1,
         },
     },
    'content': {
        'plugins': ['TextPlugin', 'PicturePlugin'],
        'text_only_plugins': ['LinkPlugin'],
        'extra_context': {"width":640},
        'name':gettext("Content"),
    },
    'right-column': {
        "plugins": ['TeaserPlugin', 'LinkPlugin'],
        "extra_context": {"width":280},
        'name':gettext("Right Column"),
        'limits': {
            'global': 2,
            'TeaserPlugin': 1,
            'LinkPlugin': 1,
        },
    },
    'base.html content': {
        "plugins": ['TextPlugin', 'PicturePlugin', 'TeaserPlugin']
    },
}

INSTALLED_APPS = (
    #'admin_tools',
    #'admin_tools.theming',
    #'admin_tools.menu',
    #'admin_tools.dashboard',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles', 
   # Uncomment the next line to enable the admin:
    'filebrowser',
    'django.contrib.admin',
    'django.contrib.flatpages',
    'cms',
    'mptt',
    'menus',
    'south',
    'sekizai',
    #'cms.plugins.file',
    #'cms.plugins.flash',
    'cms.plugins.link',
    'cms.plugins.picture',
    #'cms.plugins.teaser',
    'cms.plugins.text',
    #'cms.plugins.snippet'
    'reversion',
    'Account',
    'demo',
    'pictures',
    'upload',
    'django.contrib.formtools',
    'django.contrib.formtools.tests',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# Filebrowser settings
FILEBROWSER_MEDIA_ROOT = MEDIA_ROOT

FILEBROWSER_DIRECTORY = ""


EXTEND_CONFIG_FILE = "extend_cfg.ini"
