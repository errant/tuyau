from setuptools import setup
import os

long_description = open('README.md').read()


setup(
    name="tuyau",
    version='0.1.0',
    description="A revisit to the concept of CI/CD",
    long_description=long_description,
    keywords='build pipeline cicd',
    author='Tom Morton',
    author_email='tom@errant.me.uk',
    url='https://github.com/errant/tuyau',
    license='BSD',
    packages=['tuyau'],
    install_requires=[
        "pyparsing==2.1.8",
        "click==6"
    ],
    entry_points={
        "console_scripts": [
            "tuyau=tuyau.command:execute"
        ]
    }
)
