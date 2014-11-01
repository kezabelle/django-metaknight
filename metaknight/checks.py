# -*- coding: utf-8 -*-
from django.contrib.admin.checks import ModelAdminChecks
from django.core.checks import register
from django.core.checks import Error


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


class MKPageAdminChecks(ModelAdminChecks):
    pass
