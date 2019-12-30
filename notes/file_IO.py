# File IO

# How to run:
# open terminal in directory containing this file
# run `python3 file_IO.py`

my_file = open('test.txt')
print(my_file)

 # reads all the text within the file.
 #  read() reads the file only once. It reads using a cursor and during first read operation, the cursor reaches the end of the file because of which the other read() functions doesn't print the file contents instead black space gets out
print(my_file.read()) # prints the text
print(my_file.read()) # does nothing due to cursor issue
print(my_file.read()) # does nothing due to cursor issue

print(my_file.seek(0)) # places the cursor back to the beginning of the file

print(my_file.readline()) # reads just one line

print(my_file.readlines()) # gives a list of all the texts inside the file

# once the file is opened, we've to close it manually.
my_file.close()

# =========================================================

# use built-in `with` statement

# it opens, reads and closes the file for us.

with open('test.txt') as my_file:
	print(my_file.readlines())

# To read and write the file

with open('test.txt', mode='r+') as my_file:
	text = my_file.write('hey hey my my!')
	print(text)

# when we write something to a file, the cursor starts writing from the beginning thus overwriting any existing text

# fix is to use append mode (mode='a')

mode='a'  => appends to existing text
mode='r+' => reads and writes overwriting from beginning
mode='w'  => just writes text considering the file as empty so it deletes existing text and starts from scratch. Also, it creates a new file if one already doesn't exist

# File Paths ( accessing files stored in different locations)

# relative path
# can also do ./ or ../ etc
with open('app/test.txt', mode='r') as my_file:
	print(my_file.read())

# pathlib built-in module for file paths

# File Error Handling using Try Except block

try:
	with open('app/test.txt', mode='r') as my_file:
	print(my_file.read())
except FileNotFoundError as err:
	print('file does not exist')
	raise err
# IOError used when we want to raise an error whenever our system encounters issues during file operation
except IOError as err:
	print('IO error')
	raise err

# =========================================================

# EXERCISE

# Build a Translator

from translate import Translator

try:
	with open('test.txt', mode='r') as my_file:
		text = my_file.read()
		# print(text)
		translator = Translator(to_lang="es")
		translation = translator.translate(text)
		print(translation) # Esta es mi vida. Haré mis reglas.
except FileNotFoundError as err:
	print('file does not exist')
	raise err
except IOError as err:
	print('IO error')
	raise err

# =========================================================