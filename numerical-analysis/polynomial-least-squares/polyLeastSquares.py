import numpy as np

def polyLeastSquares(n,X,Y):
  polynomials = []           # store coefficients
  yxArray = []               # store solutions of the linear system
  for k in range(n+1):
    poly = []
    for j in range(n+1):
      xi = 0
      for i in range(len(X)):
        xi += X[i]**(j+k)
        if i==len(X)-1:
          poly.append(xi)
    yx = 0
    for z in range(len(Y)):
      yx += Y[z]*X[z]**k
    yxArray.append(yx)
    polynomials.append(poly)
  #solve linear system of equations
  a = np.array(polynomials)
  b = np.array(yxArray)
  x = np.linalg.solve(a, b)
  #print x
  return x

# test
x = [0.0,0.2,0.5,0.7,1.1,1.5,1.9,2.3,2.8,3.1]
y = [102.56,113.18,130.11,142.05,167.53,195.14,224.87,256.73,299.50,326.72]
n = 4
#polyLeastSquares(n,x,y)

# example pg 502
# x = [0,0.25,0.5,0.75,1]
# y = [1.0000,1.2840,1.6487,2.1170,2.7183]
# coefficients generated by x and y (stored in "polynomials")
# n=1 [ 1.00513714  0.86418286  0.84365714]
# n=2 [5.0, 2.5, 1.875]
# n=3 [2.5, 1.875, 1.5625]
# n=4 [1.875, 1.5625, 1.3828125]

# problem 1
# x = [0.0,0.2,0.5,0.7,1.1,1.5,1.9,2.3,2.8,3.1]
# y = [102.56,113.18,130.11,142.05,167.53,195.14,224.87,256.73,299.50,326.72]
# coefficients generated by x and y
# n=1 [ 94.19983005 72.0845177 ]
# n=2 [ 102.55284159 51.80216398 6.61821092]
# n=3 [ 1.02566282e+02 5.17290220e+01 6.68148300e+00 -1.36745636e-02]
# n=4 [ 1.02558382e+02 5.18159806e+01 6.53546812e+00 6.37479350e-02 -1.26984715e-02]
