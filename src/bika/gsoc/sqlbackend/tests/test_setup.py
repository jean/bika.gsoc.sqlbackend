# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from bika.gsoc.sqlbackend.testing import BIKA_GSOC_SQLBACKEND_INTEGRATION_TESTING  # noqa
from plone import api

import unittest2 as unittest


class TestSetup(unittest.TestCase):
    """Test that bika.gsoc.sqlbackend is properly installed."""

    layer = BIKA_GSOC_SQLBACKEND_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if bika.gsoc.sqlbackend is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('bika.gsoc.sqlbackend'))

    def test_uninstall(self):
        """Test if bika.gsoc.sqlbackend is cleanly uninstalled."""
        self.installer.uninstallProducts(['bika.gsoc.sqlbackend'])
        self.assertFalse(self.installer.isProductInstalled('bika.gsoc.sqlbackend'))

    def test_browserlayer(self):
        """Test that IBikaGsocSqlbackendLayer is registered."""
        from bika.gsoc.sqlbackend.interfaces import IBikaGsocSqlbackendLayer
        from plone.browserlayer import utils
        self.assertIn(IBikaGsocSqlbackendLayer, utils.registered_layers())
