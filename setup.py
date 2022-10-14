"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""
import os
import sys

from setuptools import setup, find_packages

# pylint: disable=redefined-builtin

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, "README.rst"), encoding="utf-8") as fid:
    long_description = fid.read()

setup(
    name="aas-core3.0rc02",
    # Synchronize with __init__.py and changelog.rst!
    version="1.0.0rc1",
    description="Manipulate, verify and de/serialize Asset Administration Shells.",
    long_description=long_description,
    url="https://github.com/aas-core-works/aas-core3.0rc02-python",
    author="Marko Ristin",
    author_email="marko@ristin.ch",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    license="License :: OSI Approved :: MIT License",
    keywords="asset administration shell sdk industry 4.0 industrie i4.0 industry iot iiot",
    packages=find_packages(exclude=["tests", "continuous_integration", "dev_scripts"]),
    install_requires=[] if sys.version_info >= (3, 8) else ["typing_extensions"],
    # fmt: off
    extras_require={
        "dev": [
            "black==22.10.0",
            "mypy==0.982",
            "pylint==2.15.4",
            "coverage>=6.5.0,<7",
            "pyinstaller>=5<6",
            "twine",
            "aas-core-meta@git+https://github.com/aas-core-works/aas-core-meta@e63c0c9#egg=aas-core-meta",
            "aas-core-codegen@git+https://github.com/aas-core-works/aas-core-codegen@4a4695c#egg=aas-core-codegen",
        ]
    },
    # fmt: on
    py_modules=["aas_core3_rc02"],
    package_data={"aas_core3_rc02": ["py.typed"]},
    data_files=[(".", ["LICENSE", "README.rst"])],
)
