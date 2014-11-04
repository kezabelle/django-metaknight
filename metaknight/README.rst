metaknight
==========

A brief explanation of how this ties things together.

``metaknight`` should likely be last, or near-last in your ``INSTALLED_APPS``
to allow the ``metaknight.admin`` module to remove and re-apply final
admin classes.

metaknight.admin
----------------

Patches `django-varlet`_ page instances to be `django-editregions`_ and
`django-adminlinks`_ compatible.

metaknight.apps
----------------

`Django 1.7+ Application`_ for registering signals between `django-varlet`_ and
`django-menuhin`_ to keep menus in sync with page creates & deletes. Older
versions won't get the signals connected automatically.

metaknight.context_processors
-----------------------------

``current_site`` Puts the ``sites.Site`` instance (for the defined ``SITE_ID``)
into the template context, as ``{{ SITE }}``

.. _django-varlet: https://github.com/kezabelle/django-varlet
.. _django-editregions: https://github.com/kezabelle/django-editregions
.. _django-adminlinks: https://github.com/kezabelle/django-adminlinks
.. _Django 1.7+ Application: https://docs.djangoproject.com/en/stable/ref/applications/
.. _django-menuhin: https://github.com/kezabelle/django-menuhin
