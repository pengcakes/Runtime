"""
This library runs the code statement 1Mil times (default) and returns the minimum time.

timeit.timeit(stmt, setup,timer, number)

    stmt: This will take the code for which you want to measure the execution time. The default value is "pass".
    setup: This will have setup details that need to be executed before stmt. The default value is "pass."
    timer: This will have the timer value, timeit() already has a default value set, and we can ignore it.
    number: The stmt will execute as per the number is given here. The default value is 1000000.

https://docs.python.org/3/library/timeit.html
https://www.guru99.com/timeit-python-examples.html
https://www.geeksforgeeks.org/timeit-python-examples/
"""
import timeit

# simple examples first
print("The time taken is ",timeit.timeit(stmt='a=10;b=10;sum=a+b'))

# can also use triple quotes
import_module = "import random"
testcode = '''
def test():
    return random.randint(10, 100)
'''
print(timeit.repeat(stmt=testcode, setup=import_module))





# binary search function
def binary_search(mylist, find):
	while len(mylist) > 0:
		mid = (len(mylist))//2
		if mylist[mid] == find:
			return True
		elif mylist[mid] < find:
			mylist = mylist[:mid]
		else:
			mylist = mylist[mid + 1:]
	return False


# linear search function
def linear_search(mylist, find):
	for x in mylist:
		if x == find:
			return True
	return False


# compute binary search time
def binary_time():
	SETUP_CODE = '''
from __main__ import binary_search
from random import randint'''

	TEST_CODE = '''
mylist = [x for x in range(10000)]
find = randint(0, len(mylist))
binary_search(mylist, find)'''

	# timeit.repeat statement
	times = timeit.repeat(setup = SETUP_CODE,
						stmt = TEST_CODE,
						repeat = 3,
						number = 10000)

	# priniting minimum exec. time
	print('Binary search time: {}'.format(min(times)))


# compute linear search time
def linear_time():
	SETUP_CODE = '''
from __main__ import linear_search
from random import randint'''

	TEST_CODE = '''
mylist = [x for x in range(10000)]
find = randint(0, len(mylist))
linear_search(mylist, find)
	'''
	# timeit.repeat statement
	times = timeit.repeat(setup = SETUP_CODE,
						stmt = TEST_CODE,
						repeat = 3,
						number = 10000)

	# priniting minimum exec. time
	print('Linear search time: {}'.format(min(times)))

if __name__ == "__main__":
	linear_time()
	binary_time()
