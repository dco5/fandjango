from warnings import warn

from django.conf import settings

FACEBOOK_APPLICATION_ID = getattr(settings, 'FACEBOOK_APPLICATION_ID')
FACEBOOK_APPLICATION_SECRET_KEY = getattr(settings, 'FACEBOOK_APPLICATION_SECRET_KEY')

try:
    FACEBOOK_APPLICATION_CANVAS_URL = getattr(settings, 'FACEBOOK_APPLICATION_CANVAS_URL')
except AttributeError:
    FACEBOOK_APPLICATION_CANVAS_URL = getattr(settings, 'FACEBOOK_APPLICATION_URL')
    warn('FACEBOOK_APPLICATION_URL is deprecated. Please use FACEBOOK_APPLICATION_CANVAS_URL instead.', DeprecationWarning)

DISABLED_PATHS = getattr(settings, 'FANDJANGO_DISABLED_PATHS', [])
ENABLED_PATHS = getattr(settings, 'FANDJANGO_ENABLED_PATHS', [])
AUTHORIZATION_DENIED_VIEW = getattr(settings, 'FANDJANGO_AUTHORIZATION_DENIED_VIEW', 'fandjango.views.authorization_denied')

FACEBOOK_APPLICATION_INITIAL_PERMISSIONS = getattr(settings, 'FACEBOOK_APPLICATION_INITIAL_PERMISSIONS', None)
