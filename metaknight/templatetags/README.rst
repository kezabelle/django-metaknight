metaknight.templatetags
=======================

csspath
-------

``{% csspath %}`` is a template tag which takes ``request.path``
(or any ``/`` delimited string) and turns it into a space separated list of
values appropriate for putting into your HTML page as CSS namespaces::

    {% load csspath %}
    <body class="{% csspath request.path '-' 'prefix--' '__suffix' %}">

Would output something like::

    <body class="prefix--root__suffix prefix--child__suffix prefix--child--grandchild__suffix">

Omitting everything but the ``request.path``/string to handle yields sensible defaults::

    <body class="path-root path-child path-child-grandchild">

The above examples are assuming the ``request.path`` was ``/child/grandchild/``


simple_csspath
--------------

A template filter which does much the same as ``{% csspath %}`` but without
the configuration options, and may clash with existing CSS class names::

    {% load csspath %}
    <body class="{{ request.path|simple_csspath }}">

with a ``request.path`` of ``/a/b/c/d/e/``, you'd get something like::

    <body class="a a-b a-b-c a-b-c-d a-b-c-d-e">
