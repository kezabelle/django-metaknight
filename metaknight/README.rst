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

.. _django-varlet: https://github.com/kezabelle/django-varlet
.. _django-editregions: https://github.com/kezabelle/django-editregions
.. _django-adminlinks: https://github.com/kezabelle/django-adminlinks
