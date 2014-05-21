from polyLeastSquares import *

def e(n,x,y,a0,a1):
  res = []
  for k in range(n+1):
    res.append((y[k] - (a1*x[k]+a0))**2)
  return res

x = [0.0,0.2,0.5,0.7,1.1,1.5,1.9,2.3,2.8,3.1]
y = [102.56,113.18,130.11,142.05,167.53,195.14,224.87,256.73,299.50,326.72]
n = 1
z = polyLeastSquares(n,x,y)

print "a0,a1",z
#z[0]=a0
#z[1]=a1
print "E",e(n,x,y,z[0],z[1])
