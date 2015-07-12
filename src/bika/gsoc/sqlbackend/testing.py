# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import bika.gsoc.sqlbackend


class BikaGsocSqlbackendLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=bika.gsoc.sqlbackend)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'bika.gsoc.sqlbackend:default')


BIKA_GSOC_SQLBACKEND_FIXTURE = BikaGsocSqlbackendLayer()


BIKA_GSOC_SQLBACKEND_INTEGRATION_TESTING = IntegrationTesting(
    bases=(BIKA_GSOC_SQLBACKEND_FIXTURE,),
    name='BikaGsocSqlbackendLayer:IntegrationTesting'
)


BIKA_GSOC_SQLBACKEND_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(BIKA_GSOC_SQLBACKEND_FIXTURE,),
    name='BikaGsocSqlbackendLayer:FunctionalTesting'
)


BIKA_GSOC_SQLBACKEND_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        BIKA_GSOC_SQLBACKEND_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='BikaGsocSqlbackendLayer:AcceptanceTesting'
)
