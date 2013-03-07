from setuptools import setup, find_packages
import sys, os

import logging, multiprocessing

version = '0.1'

setup(name='tw2.jqueryFileTree',
      version=version,
      description="",
      author='Robert Sudwarts',
      author_email='robert.sudwarts@gmail.com',
      url='',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      namespace_packages = ['tw2'],
      zip_safe=False,
      install_requires=[
        "tw2.core>=2.0b2",
        "tw2.jquery",
      ],
      entry_points="""
        [tw2.widgets]
        # Register your widgets so they can be listed in the WidgetBrowser
        widgets = tw2.jqueryFileTree
      """,
      keywords=[
        'toscawidgets.widgets',
        'qrcode',
      ],
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
)
