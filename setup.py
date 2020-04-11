"""Setup file for packages."""

from setuptools import find_packages
from setuptools import setup

required = [
    # please keep alphabetized
    "flask",
    "gunicorn",
    "pyrebase"
]

setup(name='sensehealth',
      version='0.0.0',
      description='backend for SenseHealth.',
      url='https://github.com/adibellathur/sensehealth-backend.git',
      author=('everyone'),
      author_email=['adibellathur@gmail.com'], # add your emails over here
      license='MIT',
      packages=find_packages(where='src'),
      package_dir={'': 'src'},
      install_requires=required,
      zip_safe=False)
