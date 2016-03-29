"""
File: <heaviside.py>

Copyright (c) 2016 Krystal Lee

License: MIT

<Test heaviside function>
"""

def H(x):
	if(x < 0):
		return 0
	elif(x >= 0):
		return 1

def test_H():
	print('H(-10) : %d' % H(-10))
	print('H(-10^-15) : %d' % H(pow(-10,-15)))
	print('H(0) : %d' % H(0))
	print('H(10) : %d' % H(10))

test_H()
