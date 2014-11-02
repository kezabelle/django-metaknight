# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.admin.sites import NotRegistered
from varlet.admin import PageAdminConfig
from varlet.models import Page
from editregions.admin.inlines import EditRegionInline
from adminlinks.admin import AdminlinksMixin
try:
    from .checks import MKPageAdminChecks
except ImportError:
    def MKPageAdminChecks():
        return True


class MKPageAdmin(PageAdminConfig, AdminlinksMixin, admin.ModelAdmin):
    inlines = [EditRegionInline]
    checks_class = MKPageAdminChecks

try:
    admin.site.unregister(Page)
except NotRegistered:
    pass
admin.site.register(Page, MKPageAdmin)
