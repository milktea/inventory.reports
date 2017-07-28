# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import inventory.reports


class InventoryReportsLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=inventory.reports)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'inventory.reports:default')


INVENTORY_REPORTS_FIXTURE = InventoryReportsLayer()


INVENTORY_REPORTS_INTEGRATION_TESTING = IntegrationTesting(
    bases=(INVENTORY_REPORTS_FIXTURE,),
    name='InventoryReportsLayer:IntegrationTesting'
)


INVENTORY_REPORTS_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(INVENTORY_REPORTS_FIXTURE,),
    name='InventoryReportsLayer:FunctionalTesting'
)


INVENTORY_REPORTS_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        INVENTORY_REPORTS_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='InventoryReportsLayer:AcceptanceTesting'
)
