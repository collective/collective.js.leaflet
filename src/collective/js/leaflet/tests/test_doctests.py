from collective.js.leaflet.testing import CJL_FUNCTIONAL_TESTING
from plone.testing import layered
import doctest
import glob
import logging
import os
import unittest2 as unittest

optionflags = (doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE)


def test_suite():
    logger = logging.getLogger('collective.js.leaflet.tests')
    cwd = os.path.dirname(__file__)
    files = []
    try:
        files = glob.glob(os.path.join(cwd, '*txt'))
    except Exception:
        logger.warn('No doctests for collective.js.leaflet')
    suite = unittest.TestSuite()
    globs = globals()
    for s in files:
        suite.addTests([
            layered(
                doctest.DocFileSuite(
                    s,
                    globs=globs,
                    module_relative=False,
                    optionflags=optionflags,
                ),
                layer=CJL_FUNCTIONAL_TESTING
            ),
        ])
    return suite

# vim:set ft=python:
