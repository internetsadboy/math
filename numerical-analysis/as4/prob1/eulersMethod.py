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

# dx/dt
def poly(x,t):
  return t - (2.0*x)

def EulersMethod(log,steps):
  # store data points
  D = []
  # collect data points
  T = []
  X = []
  # initial values
  n = steps
  d = [0.0,2.0]
  h = (d[1]-d[0])/n
  x = 1.0
  t = 0.0
  for k in range(int(n)):
    t = k*h                #bread
    T.append(t)
    if log:
      print "k             ", k
      print "h             ", h
      print "t             ", t
      print "x(k)          ", x
      print "hf(t(k),x(k)) ", h*poly(x,t)
    X.append(x)
    x = x+h*poly(x,t)      #butter
    if k == n-1:
      T.append(2.0)
      X.append(x)
    if log:
      print "x(k+1)        ", x
      print ""
  D.append(T)
  D.append(X)
  return D