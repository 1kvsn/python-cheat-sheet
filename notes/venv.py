# Virtual Envs in Python

# venv is standard built-in module 

# install venv in Ubuntu as it is packaged separately
$ sudo apt-get install python3-venv

# create virtual env, if the path is not present, new will be created
$ python3.8 -m venv ~/path/to/virtual/env

# active the newly created virtual env
$ source ~/path/to/virtual/env/bin/activate

# if venv not working on Ubuntu/Debian systems, refer:
https://stackoverflow.com/questions/39539110/pyvenv-not-working-because-ensurepip-is-not-available