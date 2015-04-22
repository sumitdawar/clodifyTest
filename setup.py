__author__ = 'guym'

from setuptools import setup


setup(
    zip_safe=True,
    name='cloudify-mogi-plugin',
    version='1.0',
    author='guym',
    author_email='guym@gigaspaces.com',
    packages=[
        'lib'
    ],
    license='LICENSE',
    description='Playground plugins',
    install_requires=[
    ]
)