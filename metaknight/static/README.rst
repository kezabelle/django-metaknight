provided static assets
======================

``crossdomain_nopermission.xml`` is a copy of the
`least permissive cross-domain access policy`_ provided by `Adobe`_. It should
be mounted in your webserver as ``/crossdomain.xml``, an `Apache`_ example::

    Alias /crossdomain.xml /path/to/my/collected/static/crossdomain_nopermission.xml

There is no more permissive version bundled, because to do so would be a
security risk.

.. _least permissive cross-domain access policy: https://www.adobe.com/devnet/adobe-media-server/articles/cross-domain-xml-for-streaming.html
.. _Adobe: https://www.adobe.com/
.. _Apache: https://httpd.apache.org/
