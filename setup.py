#!/usr/bin/env python

from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))
requires = []
with open(os.path.join(here, 'requirements.txt')) as f:
    for line in f.read().splitlines():
        if line.find('--') == -1:
            requires.append(line)

setup(
    name='modelutils',
    version='1.0.2',
    description='Generic statistical and modelling utilities',
    author='Mike Pappas',
    install_requires=requires,
    namespace_packages=['modelutils'],
    packages=find_packages(include=['modelutils', 'modelutils.*']),
    include_package_data=True
)
