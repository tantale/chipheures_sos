#!/usr/bin/env python
# coding: utf-8
import io
import os
import re

from setuptools import find_packages
from setuptools import setup

install_requires = [
    "Click",
]

tests_require = []

extras_require = {"test": tests_require}


def read(filename):
    filename = os.path.join(os.path.dirname(__file__), filename)
    with io.open(filename, mode="r", encoding="utf-8") as fd:
        return re.sub(r":[a-z]+:`~?(.*?)`", r"``\1``", fd.read())


setup(
    # --- identity
    name="ChipHeures_SOS",
    version="20.0.1",
    # --- description
    description="Tool for database maintenance of the Chip'heures web application",
    long_description=u"{readme}\n{changes}".format(readme=read("README.rst"), changes=read("CHANGELOG.rst")),
    long_description_content_type="text/x-rst",
    author="Laurent LAPORTE",
    author_email="tantale.solutions@gmail.com",
    url="",
    download_url="",
    license="MIT",
    platforms=["posix", "nt"],
    keywords="database, sqlite, maintenant, intranet, web, application",
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Operating System :: Unix",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Topic :: Utilities",
    ],
    # --- packaging
    install_requires=install_requires,
    packages=find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    # --- test configuration
    tests_require=tests_require,
    extras_require=extras_require,
    entry_points={"console_scripts": ["chipheures_sos = chipheures_sos.cli:cli"]},
    python_requires=">=2.7, <3",
)
