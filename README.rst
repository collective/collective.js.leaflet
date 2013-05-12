============
Introduction
============

.. contents::

Description
===========

Enrich your Plone site with the power of Leaflet maps.

This addon registers the Leaflet base Javascript and CSS resources and
optionally some interesting Leaflet plugins. By installing this addon, the base
Leaflet mapping resources are automatically integrated. To activate some of the
Plugins, you have to add one of these resource bundles to your registry.xml
Registration:

    - leaflet.markercluster
    - leaflet.fullscreen
    - leaflet.zoomfs
    - leaflet.geosearch
    - leaflet.geosearch.openstreetmap
    - leaflet.geosearch.bing
    - leaflet.geosearch.esri
    - leaflet.geosearch.google
    - leaflet.geosearch.nokia
    - leaflet.draw
    - leaflet.stamen

Since this addon only provides Leaflet resources, you have finally provide some
HTML markup for the map and write your custom Javascript integration code for
Leaflet maps to work.

You have an example view at /@@LeafletMapView.

You can watch a demo video here: `Youtube DEMO
<http://www.youtube.com/watch?v=cVOQkhmUffg>`_.


Credits
=======

Companies
---------
|makinacom|_

  * `Planet Makina Corpus <http://www.makina-corpus.org>`_
  * `Contact us <mailto:python@makina-corpus.org>`_

.. |makinacom| image:: http://depot.makina-corpus.org/public/logo.gif
.. _makinacom:  http://www.makina-corpus.com


Authors
-------

- kiorky  <kiorky@cryptelium.net>


Contributors
------------

- Eric BREHAULT <eric.brehault@makina-corpus.com>

- Johannes Raggam <dev@programmatic.pro>
