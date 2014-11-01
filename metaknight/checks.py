# -*- coding: utf-8 -*-
from django.contrib.admin.checks import ModelAdminChecks
from django.core.checks import register
from django.core.checks import Error
from django.core.checks import Warning


@register()
def adminlinks_installed(app_configs, **kwargs):
    errors = []
    from django.conf import settings
    if 'adminlinks' not in settings.INSTALLED_APPS:
        errors.append(Error(
            "Cannot use `metaknight` without `adminlinks`",
            hint="put `adminlinks` in your INSTALLED_APPS", obj=None,
            id='metaknight.E1'))
    return errors


@register()
def csp_polcy(app_configs, **kwargs):
    errors = []
    from django.conf import settings
    if 'csp.middleware.CSPMiddleware' not in settings.MIDDLEWARE_CLASSES:
        errors.append(Warning(
            "You don't appear to be using a Content-Security policy",
            hint="put `csp.middleware.CSPMiddleware` in your "
                 "MIDDLEWARE_CLASSES, as late as possible", obj=None,
            id='metaknight.W1'))
    return errors


class MKPageAdminChecks(ModelAdminChecks):
    pass
