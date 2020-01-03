# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "reasoner_server"
VERSION = "0.9.2"

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
    keywords=["OpenAPI", "NCATS Translator Reasoner API Wrapper for the Knowledge Beacon Aggregator"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['reasoner_api/API/TranslatorReasonersAPI.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['reasoner_server=reasoner_server.__main__:main']
    },
    long_description="""\
    NCATS Biomedical Translator Reasoner API Wrapping the NCATS Knowledge Beacon Aggregator API
    """
)
