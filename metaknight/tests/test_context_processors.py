# -*- coding: utf-8 -*-
from django.contrib.sites.models import Site
from django.test import TestCase as DbTest
from django.test import RequestFactory
# from django.test import SimpleTestCase as Test
from metaknight.context_processors import current_site


class StatusCodeTestCase(DbTest):
    def test_context_processor(self):
        request = RequestFactory().get('/')
        result = current_site(request)
        self.assertIn('SITE', result)
        self.assertEqual(result['SITE'], Site.objects.get_current())
