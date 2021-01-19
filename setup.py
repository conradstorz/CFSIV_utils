"""Minimal setup file for tasks project."""

from setuptools import setup, find_packages

setup(
    name='CFSIV_utils',
    version='0.1.0',
    license='proprietary',
    description='File handling and Time manipulation utilities',

    author='Conrad F. Storz IV',
    author_email='conradstorz@gmail.com',
    url='website.not.applicable.com',

    packages=find_packages(where='src'),
    package_dir={'': 'src'},

    install_requires=['pytest'],
)
