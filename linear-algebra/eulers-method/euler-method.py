# Euler's Method
# http://en.wikipedia.org/wiki/Euler_method
# user input: n, d, x, and poly 
# poly: dx/dt == f(t,x)
# n: # of steps 
# d: domain a <= t <= b
# x: initial value 
# h: step size
# t: the delta of current steps taken

from __future__ import division
from math import *
n = 4
d = [0,2]
h = d[0]+d[1]/n
t = 0

def poly(x,t):
	return x - pow(t,2) + 1

def EulersMethod():
	x = 0.5
	for k in range(n):
		t = k*h
		x = h*poly(x,t)+x
	return x

print EulersMethod() # 4.4375