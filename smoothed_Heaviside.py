"""
File: <smoothed_Heaviside.py>

Copyright (c) 2016 Krystal Lee

License: MIT

<test smoothed_Heaviside function>
"""

import math

def H_eps(x, eps=0.01):
	if(x < -eps):
		return 0
	elif(-eps <= x and x <= eps):
		return (1.0/2.0) + float(x/(2.0*eps)) + float((1.0/(2.0*math.pi)) * math.sin((math.pi*x)/eps))
	elif(eps < x):
		return 1

def test_H_eps():
	print('x < -e : %f' % H_eps(-1))
	print('x = -e : %f' % H_eps(-0.01))
	print('x = 0 : %f' % H_eps(0))
	print('x = e : %f' % H_eps(0.01))
	print('x > e : %f' % H_eps(1))

test_H_eps()
