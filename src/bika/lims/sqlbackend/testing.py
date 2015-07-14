# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import bika.lims.sqlbackend


class BikaGsocSqlbackendLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=bika.lims.sqlbackend)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'bika.lims.sqlbackend:default')


BIKA_LIMS_SQLBACKEND_FIXTURE = BikaGsocSqlbackendLayer()


BIKA_LIMS_SQLBACKEND_INTEGRATION_TESTING = IntegrationTesting(
    bases=(BIKA_LIMS_SQLBACKEND_FIXTURE,),
    name='BikaGsocSqlbackendLayer:IntegrationTesting'
)


BIKA_LIMS_SQLBACKEND_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(BIKA_LIMS_SQLBACKEND_FIXTURE,),
    name='BikaGsocSqlbackendLayer:FunctionalTesting'
)


BIKA_LIMS_SQLBACKEND_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        BIKA_LIMS_SQLBACKEND_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='BikaGsocSqlbackendLayer:AcceptanceTesting'
)
