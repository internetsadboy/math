# Euler's Method
# http://en.wikipedia.org/wiki/Euler_method
# user input: n, d, x, and poly 
# poly: dx/dt == f(t,x)
# n: # of steps 
# d: domain a <= t <= b
# x: x0
# h: step size
# t: the delta of current steps taken

from math import *

# initial values
n = 10.0
d = [0.0,2.0]
h = (d[1]-d[0])/n

def poly(x,t):
  return t - (2.0*x)

def EulersMethod(log):
  x = 1.0
  t = 0.0
  for k in range(int(n)):
    t = k*h                #bread
    if log:
      print "k             ", k
      print "h             ", h
      print "t             ", t
      print "x(k)          ", x
      print "hf(t(k),x(k)) ", h*poly(x,t)
    x = x+h*poly(x,t)      #butter
    if log:
      print "x(k+1)        ", x
      print ""
  return x

z = EulersMethod(True)
l = len(str(z))+9
for i in range(l):
  import sys
  sys.stdout.write("=")
print ""
print "x(",int(n)-1,") =", z