import unittest
import testing_python # the file which contains the functions we're testing

class TestMain(unittest.TestCase):

	# setUp() will run before every test function written below. Can be used to take actions before running every test function
	def setUp(self):
		print('about to test a function')

	def test_do_stuff(self):
		test_param = 10
		result = testing_python.do_stuff(test_param) # is the returned result from the function we're testing
		self.assertEqual(result, 15) # 15 is the result we're expecting and are checking if that is what the function returns
	
	def test_do_stuff2(self):
		# we're checking what happens when we pass a string instead of a integer
		test_param = 'jfjfdf'
		result = testing_python.do_stuff(test_param)
		# we're checking if the except block is working as expected
		# the except block is returning the err and we're checking if that err is an instance of ValueError object
		self.assertIsInstance(result, ValueError)

	def test_do_stuff3(self):
		test_param = None
		result = testing_python.do_stuff(test_param)
		self.assertEqual(result, 'please enter a number')
	
	def test_do_stuff4(self):
		test_param = ''
		result = testing_python.do_stuff(test_param)
		self.assertEqual(result, 'please enter a number')
	
	def test_do_stuff5(self):
		test_param = 0
		result = testing_python.do_stuff(test_param)
		self.assertEqual(result, 5)
	
	# used to run a function after every test function
	def tearDown(self):
		print('cleaning up')

if __name__ == '__main__':
	unittest.main() # this main has nothing to do with the main file. It just tells python to run the tests if this is the file which is running it


# command: `python3 -m unittest` this will execute all the test files.

# command: `python3 -m unittest -v` prints more verbose information

# ============================================================================================