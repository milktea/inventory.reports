# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from inventory.reports.testing import INVENTORY_REPORTS_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that inventory.reports is properly installed."""

    layer = INVENTORY_REPORTS_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if inventory.reports is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'inventory.reports'))

    def test_browserlayer(self):
        """Test that IInventoryReportsLayer is registered."""
        from inventory.reports.interfaces import (
            IInventoryReportsLayer)
        from plone.browserlayer import utils
        self.assertIn(
            IInventoryReportsLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = INVENTORY_REPORTS_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['inventory.reports'])

    def test_product_uninstalled(self):
        """Test if inventory.reports is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'inventory.reports'))

    def test_browserlayer_removed(self):
        """Test that IInventoryReportsLayer is removed."""
        from inventory.reports.interfaces import \
            IInventoryReportsLayer
        from plone.browserlayer import utils
        self.assertNotIn(
           IInventoryReportsLayer,
           utils.registered_layers())
