# -*- coding: utf-8 -*-
import logging
from django.apps import AppConfig


logger = logging.getLogger(__name__)


class MKAppConfig(AppConfig):
    name = 'metaknight'
    verbose_name = "CMS"

    def ready(self):
        from django.db.models.signals import post_save, pre_delete
        from menuhin.listeners import create_menu_url, unpublish_on_delete
        from varlet.models import Page
        post_save.connect(sender=Page, receiver=create_menu_url,
                          dispatch_uid="create_menuitem_from_page")
        pre_delete.connect(sender=Page, receiver=unpublish_on_delete,
                           dispatch_uid="unpublish_menuitem_from_page_delete")
