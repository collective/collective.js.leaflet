import os
from setuptools import setup, find_packages

version = '0.7'


def read(*rnames):
    return open(
        os.path.join('.', *rnames)
    ).read()

long_description = "\n\n".join(
    [read('README.rst'),
     read('docs', 'INSTALL.rst'),
     read('docs', 'CHANGES.rst'),
    ]
)

classifiers = [
    "Framework :: Plone",
    #"Framework :: Plone :: 4.0", # no ResourceRegistries>=2.1a1
    #"Framework :: Plone :: 4.1", # no ResourceRegistries>=2.1a1
    "Framework :: Plone :: 4.2",
    "Framework :: Plone :: 4.3",
    "Programming Language :: Python",
    "Topic :: Software Development"
]

name = 'collective.js.leaflet'
setup(
    name=name,
    namespace_packages=['collective', 'collective.js'],
    version=version,
    description='Leaflet maps integration for Plone',
    long_description=long_description,
    classifiers=classifiers,
    keywords='plone leaflet gis geo',
    author='kiorky',
    author_email='kiorky@cryptelium.net',
    url='http://pypi.python.org/pypi/%s' % name,
    license='GPL',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    install_requires=[
        'setuptools',
        'z3c.autoinclude',
        'Plone',
        'Products.ResourceRegistries>=2.1a1',
    ],
    extras_require={
        'test': ['plone.app.testing']
    },
    entry_points={
        'z3c.autoinclude.plugin': ['target = plone'],
    },
)
# vim:set ft=python:
