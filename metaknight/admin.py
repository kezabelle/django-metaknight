# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.admin.sites import NotRegistered
from django.contrib.sites.models import Site
from menuhin.models import MenuItem
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

    def get_ancestors(self, obj):
        """
        This is horribly expensive!
        It gets worse the further into the ancestry one has to go.
        At a minimum it'll be ... 2 queries? With no real maximum bound.
        """
        pages = []
        try:
            item = MenuItem.objects.get(uri=obj.get_absolute_url(),
                                        site=Site.objects.get_current())
        except (MenuItem.DoesNotExist, MenuItem.MultipleObjectsReturned) as e:
            return pages
        for x in item.get_ancestors():
            page_slug = x.get_absolute_url().strip('/')
            # our pages are FLAT so we can skip anything still with a path.
            if page_slug.count('/') > 0:
                continue
            # special case the homepage :(
            if page_slug == "":
                try:
                    self.model.objects.get_homepage()
                except self.model.DoesNotExist:
                    continue

            # slug could match a non-homepage page, so we look it up ...
            try:
                page = self.model.objects.get(slug=page_slug)
            except self.model.DoesNotExist:
                continue
            pages.append(page)
        return pages

try:
    admin.site.unregister(Page)
except NotRegistered:
    pass
admin.site.register(Page, MKPageAdmin)
