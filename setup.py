# Copyright 2016 Fabian Wenzelmann

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup, find_packages

setup(
    name='django-bootstrap3-multidatepicker',
    version='0.1.2',
    description='Datepicker that supports the selection of multiple dates for Django, using Bootstrap Twitter.',
    long_description=open('README.rst').read(),
    author='Fabian Wenzelmann',
    author_email='fabianwenzelmann@posteo.de',
    url='https://github.com/FabianWe/django-bootstrap3-multidatepicker',
    license='Apache Software License',
    classifiers = [
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Operating System :: OS Independent',
        'Environment :: Web Environment',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Framework :: Django :: 1.9',
        'Framework :: Django',
        'Intended Audience :: Developers',
    ],
    keywords='django calendar multidate',
    packages=find_packages(),
    install_requires=['Django', 'django-bootstrap3',],
    include_package_data=True
)
