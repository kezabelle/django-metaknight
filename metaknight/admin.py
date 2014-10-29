# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.admin.sites import NotRegistered
from varlet.admin import PageAdminConfig
from varlet.models import Page
from editregions.admin.inlines import EditRegionInline


class MKPageAdmin(PageAdminConfig, admin.ModelAdmin):
    inlines = [
        EditRegionInline,
    ]

try:
    admin.site.unregister(Page)
except NotRegistered:
    pass
admin.site.register(Page, MKPageAdmin)
