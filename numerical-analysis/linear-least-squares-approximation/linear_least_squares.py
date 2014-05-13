# discrete least squares approximation
# http://en.wikipedia.org/wiki/Least_squares
# objective:
# generate the 'best' linear approximation while minimizing error (weight of data points)
# minimize the total error of the collection (xi,yi) from i = 1 to m

def leastSquares(n,R):
  x = 0
  y = 0
  x2 = 0
  xy = 0
  k = 1
  # compute summations
  while k <= n:
    x += k
    y += R[k-1]
    x2 += k*k
    xy += k*R[k-1]
    k+=1
  # compute a0, a1 in order to compute P(xi) in E
  a = a0(x,x2,y,xy,n)
  b = a1(x,x2,y,xy,n)
  return E(a,b,n,R)

def a0(x,x2,y,xy,n):
  return (x2*y-xy*x)/(n*x2-x**2)

def a1(x,x2,y,xy,n):
  return (n*xy-x*y)/(n*x2-x**2)

def E(a0,a1,n,R):
  k = 1
  p = 0
  E = 0
  X = []
  Y = []
  # generate 'best' approximations for yi using P(xi)
  while k <= n:
    p = a1*k+a0
    E += (R[k-1]-p)**2
    X.append(k)
    Y.append(p)
    k+=1
  return [E,X,Y]

# initial values
r = [1.3,3.5,4.2,5.0,7.0,8.8,10.1,12.5,13.0,15.6]  # range
n = 10                                             # size of collection
print leastSquares(n,r)                            # error, {(xi,yi)} from i = 1 to n
