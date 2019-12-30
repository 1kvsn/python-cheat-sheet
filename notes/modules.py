# Modules

# modules means files
# packages means folders

import utils # importing utils.py file from the same directory
print(utils.mul(2,3)) # imported files can be used this way

# Different ways to import

import module
from package.subpackage import module
from package.module import func1, func2 # this way we can know what exactly we've imported
from package import *

# =================================================================================

# What is
if __name == __main__

        #^^^^^ notice double equals

# __main__ is the name of the file which is being executed

# every module file gets __name__ equals to the file name

# to ensure, a block of code is only executed if the executing file is the __main__ file, we use the condition

if __name == __main__:
    # rest code goes here

# For e.g

# when type checking is done for class etc, it shows as <class __main__.className>

# this indicates that the class is being executed from the __main__ file. If it was any other file, that file name will appear there

# ====================================================================================

# Importing built-in modules

import random

print(dir(random)) # shows all available methods

# ====================================================================================

# Python Package Index

pip install _package__name
pip3 list # lists all installed packages
pip3 install pyjokes==0.4.0 # to install a specific version
pip3 uninstall __package__name 
pip3 -V # checks for current version

#pipenv to have different versions of packages for a project

# Useful modules #

from collections import Counter, defaultdict, OrderedDict

li = [1,2,3,4,5,6,7,7]
print(Counter(li))

sentence = 'blah blah blah thinking about Python programming'
print(Counter(sentence)) # counts the number of iterances of letters in sentence and prints them out in the form of a dict

# =================================================================================

# Debugging in Python

import pdb

def add(n1, n2):
    pdb.set_trace() # where the execution gets paused
    return n1*n2

add(3,4)

# help within pdb to see list of methods.
# help _method_name to know more about a method
# can pause the execution at a line to allow us to debug
# check arguments and their values
# reassign arguments while Debugging
# step over to next line 

https://docs.python.org/3/library/pdb.html

# =================================================================================