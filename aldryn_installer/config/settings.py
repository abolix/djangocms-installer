# -*- coding: utf-8 -*-
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.transaction.TransactionMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.i18n",
    "django.core.context_processors.debug",
    "django.core.context_processors.request",
    "django.core.context_processors.media",
    'django.core.context_processors.csrf',
    "django.core.context_processors.tz",
    "cms.context_processors.media",
    "sekizai.context_processors.sekizai",
    "django.core.context_processors.static",
)

TEMPLATE_DIRS = (
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'south',
    'sekizai',
    'cms',
    'menus',
    'mptt',
)

STANDARD_PLUGINS = (
    'cms.plugins.file',
    'cms.plugins.flash',
    'cms.plugins.googlemap',
    'cms.plugins.inherit',
    'cms.plugins.link',
    'cms.plugins.picture',
    'cms.plugins.teaser',
    'cms.plugins.video',
)

FILER_PLUGINS = (
    'cmsplugin_filer_file',
    'cmsplugin_filer_folder',
    'cms.plugins.flash',
    'cms.plugins.googlemap',
    'cms.plugins.inherit',
    'cmsplugin_filer_link',
    'cmsplugin_filer_teaser',
    'cmsplugin_filer_video',
    'cmsplugin_filer_utils',
)

CMS_3_HEAD = (
    'djangocms_admin_style',
    'djangocms_text_ckeditor',
)

CMS_3_APPLICATIONS = (
    'cms.stacks',
    'djangocms_style',
    'djangocms_column',
)

CMS_2_APPLICATIONS = (
    'cms.plugins.text',
)

REVERSION_APPLICATIONS = (
    'reversion',
)

CMS_TEMPLATES = (
    ('index.html', 'Home'),
    ('other.html', 'Other'),
)
LANGUAGES = (
)

CMS_LANGUAGES = {
    1: [
    ],
    'default': {
        'redirect_on_fallback':  True,
        'public': True,
        'hide_untranslated': False,
    }
}
CMS_PERMISSION = True
CMS_PLACEHOLDER_CONF = {}

URLCONF = {

}