from poly_least_squares_trig import *
import matplotlib.pyplot as plt

# step fxn
def f(x):
  if x <= -0.5:
    return 0.
  elif x <= 0.5:
    return 1.
  else:
    return 0.

f(-0.5) # 0
f(0.5)  # 1
f(1)    # 0

# generate polys
P0 = P(0, f)
P1 = P(1, f)
P2 = P(2, f)
P3 = P(3, f)
P4 = P(4, f)
P5 = P(5, f)
P1(1/2)

# x vals from [-1,1] and [-1.25,1.25]
x1 = generateX(400,  -1., 1.)
x2 = generateX(600, -1.25, 1.25)

# y vals
y = [f(i) for i in x1]
y0 = [P0(i) for i in x2]
y1 = [P1(i) for i in x2]
y2 = [P2(i) for i in x2]
y3 = [P3(i) for i in x2]
y4 = [P4(i) for i in x2]
y5 = [P5(i) for i in x2]

# graph
plt.figure(1)
plt.plot(x1, y, label='f')
plt.plot(x2, y0, label='1/2')
plt.plot(x2, y1, label='cos(pi*x)')
plt.plot(x2, y2, label='cos(2*pi*x)')
plt.plot(x2, y3, label='cos(3*pi*x)')
plt.plot(x2, y4, label='cos(4*pi*x)')
plt.plot(x2, y5, label='cos(5*pi*x)')
plt.axis([-1.25,1.25,-0.5,1.2])
plt.legend()
plt.show()
