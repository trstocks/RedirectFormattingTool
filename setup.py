import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name = "redirect formatter",
      version = "0.0.1",
      author = "Troy Stocks",
      author_email = "slipstreamanthem@gmail.com",
      description = ("a tool to assist with correcting/formatting the urls so that they are ready to be placed in another tool."),
      license = "BSD",
      keywords = "redirect, alias, vanity",
      packages=['package'],
      package_dir={'package': 'src/package'},
     # package_data={'package': ['data/*.dat']},
      #long_description=read('README.md'),
      install_requires=[
          'requests'
          ]
      )
