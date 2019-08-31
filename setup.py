#!/usr/bin/python3

from setuptools import setup

setup(
	name='assetfynder',
	version='0.1',
	py_modules=['main'],
	install_requires=[
		'Click',
		],
	entry_points='''
		[console_scripts]
		assetfynder=main:cli
		''',
	)
