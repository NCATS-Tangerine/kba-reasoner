# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "swagger_server"
VERSION = "1.0.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["connexion"]

setup(
    name=NAME,
    version=VERSION,
    description="NCATS Translator Reasoner API Wrapper for the Knowledge Beacon Aggregator",
    author_email="richard@starinformatics.com",
    url="",
    keywords=["Swagger", "NCATS Translator Reasoner API Wrapper for the Knowledge Beacon Aggregator"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['swagger_server=swagger_server.__main__:main']},
    long_description="""\
    NCATS Biomedical Translator Reasoner API Wrapping the NCATS Knowledge Beacon Aggregator API
    """
)

