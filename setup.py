"""Setup module for day of code package."""

from setuptools import setup

setup(
	name='day of code',
	description="Day of Code Katas",
	package_dir={'':'src'},
	author='Marco Zangari',
	author_email=('mjzangari@gmail.com'),
	py_modules=[],
	install_requires=[],
	extras_require={
	'testing': ['pytest', 'pytest-cov', 'pytest-watch', 'tox'],
	'development': ['ipython']
	},

	entry_points={
	}
)
