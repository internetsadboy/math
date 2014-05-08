# Euler's Modified Method
# http://en.wikipedia.org/wiki/Euler_method#Modifications_and_extensions 
# user input: n, d, x, and poly 
# poly: dx/dt == f(t,x)
# n: # of steps 
# d: domain a <= t <= b
# x: initial value 
# h: step size
# t: the delta of current steps taken

from math import *

n = 10.0
d = [0.0,2.0]
h = (d[1]-d[0])/n

# f(t,x) + f(t+h,x+hf(t,x))
def poly(h,x,t):
  return 4*h*x - 2*h*t - 4*x + 2*t + h

# euler stuff
def EulersModfied(log):
  x = 1.0
  t = 0.0
  for k in range(int(n)):
    t = k*h                # bread
    if log:
      print "k                 ", k
      print "h                 ", h
      print "t                 ", t
      print "x(k)              ", x
      print "h/2f(h,t(k),x(k)) ", h/2*poly(h,x,t)
    x = x+h/2*poly(h,x,t)  # butter
    if log:
      print "x(k+1)            ", x 
      print ""
  return x

z =EulersModfied(True)
l = len(str(z))+9
for i in range(l):
  import sys
  sys.stdout.write("=")
print ""
print "x(",int(n)-1,") =", z