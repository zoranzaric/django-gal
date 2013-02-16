import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name = 'django-gal',
    version = '0.1',
    packages = ['gal'],
    include_package_data = True,
    license = 'BSD License',
    description = 'A Django based image gallery.',
    long_description = README,
    url = 'https://github.com/zoranzaric/django-gal',
    author = 'Zoran Zaric',
    author_email = 'zz@zoranzaric.de',
    classifiers = [
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
    ],
)
