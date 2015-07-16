# -*- coding: utf-8 -*-
from venusianconfiguration import configure

from transmogrifier.blueprints import Blueprint
from faker import Faker

configure_blueprint = configure.transmogrifier.blueprint.component


@configure_blueprint(name='bika.gsoc.sqlbackend.mock_contacts')
class MockContacts(Blueprint):
    def __iter__(self):
        for item in self.previous:
            yield item

        amount = int(self.options.get('amount', '0'))
        fake = Faker()

        for i in range(amount):
            yield {
                'name': fake.name(),
                'address': fake.address()
            }
