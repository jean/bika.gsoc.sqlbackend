Transmogrifier Project
======================

Activation
----------

.. code:: bash

   $ pip install -r requirements.txt
   $ python setup.py develop

It's recommended to use Python (2.7 or 3.4, or greater) virtualenv_.

.. _virtualenv: https://pypi.python.org/pypi/virtualenv


Usage
-----

.. code:: bash

   $ transmogrify

.. code:: bash

   $ transmogrify --list

.. code:: bash

   $ transmogrify bika.gsoc.sqlbackend_example


Blueprints
----------

New blueprints can be registered by implementing them in ``.py``-files at
``./src/bika.gsoc.sqlbackend_blueprints/``.

Example: ``./src/bika.gsoc.sqlbackend_blueprints/mock_contacts.py``


Pipelines
---------

New named pipelines can be registered by simply adding new ``.cfg`` pipeline
file into ``./src/bika.gsoc.sqlbackend_pipelines/``.

Example: ``./src/bika.gsoc.sqlbackend_pipelines/bika.gsoc.sqlbackend_example.cfg``
