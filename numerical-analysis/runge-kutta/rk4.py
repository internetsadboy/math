# Runge-Kutta Method (RK4)
# http://en.wikipedia.org/wiki/Runge%E2%80%93Kutta_methods#The_Runge.E2.80.93Kutta_method
# n: num of steps
# d: domain
# h: step size
# f: dx/dt
# x: x0 (initialized in rk4)
# t: t0 (initialized in rk4)

from math import *

# dx/dt
def f(t,x):
	return t-(2*x)

# do rk4 magic
def rk4(log,steps):
	# collect data points (t,x) for k iterations
	T = []
	X = []
	# initial values
	n = steps
	d = [0.0,2.0]
	h = (d[1]-d[0])/n
	x = 1.0
	t = 0.0
	# get your popcorn ready
	for k in range(int(n)):
		t = k*h
		T.append(t)
		k1 = h*f(t,x)
		k2 = h*f(t+h/2,x+k1/2)
		k3 = h*f(t+h/2,x+k2/2)
		k4 = h*f(t+h,x+k3)
		X.append(x)
		x = x + (k1 + 2*k2 + 2*k3 + k4)/6  # bread and butter
		if k == n-1:
			T.append(2.0)
			X.append(x)
		if log:
			print "t  ", t
			print "k1 ", k1
			print "k2 ", k2
			print "k3 ", k3
			print "k4 ", k4
			print "x  ", x
			print ""
	return [T,X]
