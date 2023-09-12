# -*- coding: utf-8 -*-

from setuptools import setup

# def readme():
#     with open("README.md") as f:
#         return f.read()

setup(name="drawBotLab",
      version="1.0.1",
      description="Some helpers for DrawBot",
      long_description="TBD",
      classifiers=[
        "Development Status :: 4 - Beta",
        "License :: Other/Proprietary License",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development :: Build Tools",
      ],
      author="David Jonathan Ross",
      author_email="david@djr.com",
      license="All rights reserved",
      packages=[
        "drawBotLab",
        ],
      install_requires=[
        #"drawBot",

      ],
      include_package_data=True,
      zip_safe=False)
