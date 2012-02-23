# -*- coding: utf-8 -*-

import os, sys

try:
    from Products.CMFPlone.migrations import migration_util
except:
    #plone4
    from plone.app.upgrade import utils as migration_util

from Products.CMFCore.utils import getToolByName


def upgrade(portal_setup):
    """
    """
    site = portal_setup.aq_parent

    # install Products.PloneSurvey and dependencies
    #migration_util.loadMigrationProfile(site,
    #                                    'profile-Products.PloneSurvey:default')
    migration_util.loadMigrationProfile(
        site,
        'profile-collective.js.leaflet.migrations.v11:1011')

