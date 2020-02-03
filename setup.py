#!/usr/bin/env python3
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='yamz',
      version='0.1.6',
      description='An easy way to manage environment specific configuration',
      long_description=long_description,
      long_description_content_type='text/markdown',
      author='Lemuel Boyce',
      author_email='lemuelboyce@gmail.com',
      packages=['yamz'],
      url='https://github.com/rhymiz/yamz',
      include_package_data=True,
      zip_safe=False,
      license='MIT',
      python_requires='>=3.5',
      install_requires=[
          'PyYAML>=5.1'
      ],
      classifiers=[
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.5",
          "Programming Language :: Python :: 3.6",
          "Programming Language :: Python :: 3.7",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
      ])
