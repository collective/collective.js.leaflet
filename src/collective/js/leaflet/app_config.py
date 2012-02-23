#-*- coding: utf-8 -*-
"""Specific project configuration."""
GLOBALS = globals()




################################################################################
# Products that have entries in quickinstaller,
# here are their 'id' (not the translated name)
################################################################################

PRODUCT_DEPENDENCIES = (\
)

EXTENSION_PROFILES = ('collective.js.leaflet:default',)

SKIN = 'collective.js.skin'
HIDDEN_PRODUCTS = [u'plone.app.openid', u'NuPlone',
#    u'collective.js.leaflet.migrations.v1_1',
#    u'collective.js.leaflet.migrations',
]
HIDDEN_PROFILES = [u'plone.app.openid', u'NuPlone',
    u'collective.js.leaflet.migrations.v11',
    u'collective.js.leaflet.migrations',

]

from zope.interface import implements
from Products.CMFQuickInstallerTool.interfaces import INonInstallable as INonInstallableProducts
from Products.CMFPlone.interfaces import INonInstallable as INonInstallableProfiles

class HiddenProducts(object):
    implements(INonInstallableProducts)

    def getNonInstallableProducts(self):
        return HIDDEN_PRODUCTS

class HiddenProfiles(object):
    implements(INonInstallableProfiles)

    def getNonInstallableProfiles(self):
        return [ u'plone.app.openid', u'NuPlone', ]
