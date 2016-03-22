.. Django Bootstrap3 Multidatepicker documentation master file, created by
   sphinx-quickstart on Mon Mar 21 20:27:38 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Django Bootstrap3 Multidatepicker's documentation!
=============================================================

Contents:

.. toctree::
   :maxdepth: 1

About
=====

A datepicker that supports the selection of multiple dates for Django, using Bootstrap Twitter.

The aim of this package is to provide widgets and form fields for Django that use bootstrap-datepicker.
There are some packages that already try to do this, however I've never found one with working multidate support.
The package's homepage can be found here on `GitHub <https://github.com/FabianWe/django-bootstrap3-multidatepicker>`_.

I'll slightly follow the package as provide `here <https://github.com/nkunihiko/django-bootstrap3-datetimepicker>`_.
This package supports single date selection, mine will cover multidate selection.
Because that's not so much change I'll actually copy a lot from this code base.

License
=======

foodle is licensed under the `Apache License, Version 2.0 <http://www.apache.org/licenses/LICENSE-2.0>`_::

  Copyright 2016 Fabian Wenzelmann

  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.

There are many libraries used by this project, see :doc:`here <third_party>` for library license information.

Installation
============

The project is still not yet in a state ready for deployment.
I'm planning to upload the current version to pypi.

You need the following:

* python3 (tested with python 3.4.3)
* `django <https://www.djangoproject.com/>`_ (tested with 1.9.2)
* `django-bootstrap3 <https://pypi.python.org/pypi/django-bootstrap3>`_

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
