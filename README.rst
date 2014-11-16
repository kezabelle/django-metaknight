==========
Metaknight
==========

A `Django`_ application which smashes together various bits and pieces I've
written to create some sort of bastard CMS.

Currently builds on:

* `django-varlet`_ ("pages")
* `django-editregions`_ (define blocks of editable content)
* `django-menuhin`_ (trees of menus)
* `django-adminlinks`_ (frontend modal editing)

Options I might bring in, in future:

* `django-patternatlas`_ (living style guides)
* `django-churlish`_ (runtime URL [access/auth etc] configuration)
* `django-allowedsites`_ (dynamic ``ALLOWED_HOSTS``)
* `django-moreloaders`_ (semi-cached template loader, useful for editregions)

Maybe also:

* `django-urlmonitor`_ (redirects)
* `django-thadminjones`_ (a non-intrusive admin skin)
* `django-haystackbrowser`_ (browse your search indexes, only useful if using
  `django-haystack`_)

Then for security, probably also:

* `django-csp`_ (Content Security Policy bits)
* django-secure (various)
* django-p3p (p3p policy headers)
* django-cors-headers (cross-origin requests)

Build statuses
--------------

`django-editregions`_
^^^^^^^^^^^^^^^^^^^^^

.. image:: https://travis-ci.org/kezabelle/django-editregions.svg?branch=master
  :target: https://travis-ci.org/kezabelle/django-editregions

`django-menuhin`_
^^^^^^^^^^^^^^^^^

.. image:: https://travis-ci.org/kezabelle/django-menuhin.png?branch=master
  :target: https://travis-ci.org/kezabelle/django-menuhin

`django-varlet`_
^^^^^^^^^^^^^^^^

.. image:: https://travis-ci.org/kezabelle/django-varlet.svg?branch=master
  :target: https://travis-ci.org/kezabelle/django-varlet


.. _Django: https://www.djangoproject.com/
.. _django-varlet: https://github.com/kezabelle/django-varlet
.. _django-editregions: https://github.com/kezabelle/django-editregions
.. _django-churlish: https://github.com/kezabelle/django-churlish
.. _django-menuhin: https://github.com/kezabelle/django-menuhin
.. _django-urlmonitor: https://github.com/kezabelle/django-urlmonitor
.. _django-allowedsites: https://github.com/kezabelle/django-allowedsites
.. _django-patternatlas: https://github.com/kezabelle/django-patternatlas
.. _django-adminlinks: https://github.com/kezabelle/django-adminlinks
.. _django-moreloaders: https://github.com/kezabelle/django-moreloaders
.. _django-thadminjones: https://github.com/kezabelle/django-thadminjones
.. _django-haystackbrowser: https://github.com/kezabelle/django-haystackbrowser
.. _django-haystack: https://github.com/toastdriven/django-haystack

.. _django-csp: https://github.com/mozilla/django-csp
