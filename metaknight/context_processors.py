# -*- coding: utf-8 -*-
from django.contrib.sites.models import Site


def current_site(request):
    return {
        'SITE': Site.objects.get_current(),
    }
