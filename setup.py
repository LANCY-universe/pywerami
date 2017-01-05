#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

exec(open('pywerami/__init__.py').read())

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

requirements = [
    'numpy >= 1.8',
    'matplotlib >= 1.2',
    'scipy'
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='pywerami',
    version='0.2.1',
    description="pywerami is a stand-alone program to make an countour/3D plot from a contour data file generated by the Perple_X program WERAMI.",
    long_description=readme + '\n\n' + history,
    author="Ondrej Lexa",
    author_email='lexa.ondrej@gmail.com',
    url='https://github.com/ondrolexa/pywerami',
    packages=find_packages(),
    package_data={'pywerami.images': ['*.png'],
                  'pywerami.samples': ['*.tab']},
    install_requires=requirements,
    entry_points={
    'console_scripts': [
        'pywerami=pywerami.mainapp:main'
        ]
    },
    license="BSD",
    zip_safe=False,
    keywords='pywerami',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3'
    ],
    test_suite='tests',
    tests_require=test_requirements
)
