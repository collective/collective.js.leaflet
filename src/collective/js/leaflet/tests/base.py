from collective.js.leaflet.testing import CJL_FIXTURE
from collective.js.leaflet.testing import CJL_FUNCTIONAL_TESTING
from collective.js.leaflet.testing import CJL_INTEGRATION_TESTING
from collective.js.leaflet.testing import CJL_SELENIUM_TESTING
from collective.js.leaflet.testing import PLONE_MANAGER_NAME
from plone.app.testing import TEST_USER_NAME
from plone.app.testing import login
import unittest2 as unittest


class TestCase(unittest.TestCase):
    """We use this base class for all the tests in this package.
    If necessary, we can put common utility or setup code in here.
    """
    layer = CJL_FIXTURE

    def setUp(self):
        super(TestCase, self).setUp()
        self.portal = self.layer['portal']
        self.app = self.layer['app']

    def add_user(self, id, username, password, roles=None):
        self.layer.add_user(id, username, password, roles=None)

    def logout(self):
        self.layer.logout()

    def login(self, user=None):
        if not user:
            user = TEST_USER_NAME
        login(self.portal, user)

    def loginAsPortalOwner(self):
        self.layer.loginAsPortalOwner()

    def loginAsManager(self):
        self.login(PLONE_MANAGER_NAME)


class IntegrationTestCase(TestCase):
    """Integration base TestCase."""
    layer = CJL_INTEGRATION_TESTING


class FunctionalTestCase(TestCase):
    """Functionnal base TestCase."""
    layer = CJL_FUNCTIONAL_TESTING


class SeleniumTestCase(TestCase):
    """Functionnal base TestCase."""
    layer = CJL_SELENIUM_TESTING

# vim:set ft=python:
