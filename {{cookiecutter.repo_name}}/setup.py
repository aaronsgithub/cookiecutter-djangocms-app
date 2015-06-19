#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name="{{ cookiecutter.repo_name }}",
    version="{{ cookiecutter.version }}",
    packages=find_packages(),
    author="{{ cookiecutter.author }}",
    author_email="{{ cookiecutter.author_email }}"
)
