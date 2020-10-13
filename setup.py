#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
import re
from setuptools import setup
from pathlib import Path


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding="utf-8").read()


def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    version = Path(package, "__version__.py").read_text()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", version).group(1)


def get_packages(package):
    """
    Return root package and all sub-packages.
    """
    return [str(path.parent) for path in Path(package).glob("**/__init__.py")]


setup(
    name="clientapi",
    version=get_version("clientapi"),
    author="Prashanth Sams",
    author_email="sams.prashanth@gmail.com",
    maintainer="Prashanth Sams",
    maintainer_email="sams.prashanth@gmail.com",
    license="MIT",
    url="https://github.com/prashanth-sams/python-client-api",
    description="HTTP REST API client for testing APIs that binds a complete api automation framework setup within itself",
    long_description=read("README.rst"),
    keywords=["api", "test", "api test", "rest api", "test api"],
    package_data={"clientapi": ["py.typed"]},
    packages=get_packages("clientapi"),
    include_package_data=True,
    python_requires=">=3.5",
    install_requires=["pytest", "urllib3"],
    classifiers=[
        "Topic :: Software Development :: Testing",
        "Programming Language :: Python",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ]
)
