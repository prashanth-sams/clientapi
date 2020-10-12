#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
from setuptools import setup, find_packages


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding="utf-8").read()


setup(
    name="client-api",
    version="0.0.1",
    author="Prashanth Sams",
    author_email="sams.prashanth@gmail.com",
    maintainer="Prashanth Sams",
    maintainer_email="sams.prashanth@gmail.com",
    license="MIT",
    url="https://github.com/prashanth-sams/python-client-api",
    description="HTTP REST API client for testing APIs based on the pytest framework that binds a complete api automation framework setup within itself",
    long_description=read("README.rst"),
    keywords=["api", "test", "api test", "rest api", "test api", "pytest", "py.test"],
    packages=find_packages(),
    python_requires=">=3.5",
    install_requires=["pytest", "requests"],
    classifiers=[
        "Topic :: Software Development :: Testing",
        "Programming Language :: Python",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ]
)
