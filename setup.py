# coding: utf-8
# First, we try to use setuptools. If it's not available locally,
# we fall back on ez_setup.
try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

NAME = "kba_reasoner"
VERSION = "0.9.2"

LONG_DESCRIPTION = 'NIH NCATS Biomedical Translator Knowledge Beacon Reasoner API'

REQUIRES = []
with open('requirements.txt') as requirements_file:
    for line in requirements_file:
        line = line.strip()
        if len(line) == 0:
            continue
        if line[0] == '#':
            continue
        pinned_version = line.split()[0]
        REQUIRES.append(pinned_version)

setup(
    name=NAME,
    version=VERSION,
    description="Knowledge Beacon Reasoner",
    keywords=["NCATS Biomedical Translator", "Knowledge Beacon Aggregator", "KBA Reasoner API"],
    author='Richard Bruskiewich',
    author_email="richard@starinformatics.com",
    packages=find_packages(),
    package_data={},
    url="https://github.com/NCATS-Tangerine/kba-reasoner",
    download_url='https://github.com/NCATS-Tangerine/kba-reasoner',
    entry_points={
        'console_scripts': [
        ]
    },
    long_description=LONG_DESCRIPTION,
    install_requires=REQUIRES,
    setup_requires=['pytest-runner'],
    tests_require=['pytest', 'pytest-cov', 'mock'],
    license='MIT License',
    zip_safe=False,
)
