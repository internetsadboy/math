from scipy.integrate import quad
from math import cos
from math import pi

# n:numPoints,s:start,e:end
def generateX(n,s,e):
  return [((e-s)/(n-1))*i + s for i in range(n)]

# f(x)=1/2
def trig0(x):
  return 0.5

# f(x)=cos(pi*x)
def trig1(x):
  return cos(pi*x)

# f(x)=cos(2*pi*x)
def trig2(x):
  return cos(2*pi*x)

# f(x)=cos(3*pi*x)
def trig3(x):
  return cos(3*pi*x)

# f(x)=cos(4*pi*x)
def trig4(x):
  return cos(4*pi*x)

# f(x)=cos(5*pi*x)
def trig5(x):
  return cos(5*pi*x)

# associate poly with order
def TrigBasis(k,x):
  if k==0:
    return trig0(x)
  elif k==1:
    return trig1(x)
  elif k==2:
    return trig2(x)
  elif k==3:
    return trig3(x)
  elif k==4:
    return trig4(x)
  else:
    return trig5(x)

# compute ck (inner product of f(x))
def ck(f):
  def square(x):
    return f(x)**2
  return quad(square,-1,1)[0]

#compute ak, (inner product of step fxn and f(x) of order k)/(ck)
#k:order,f:fxn
def ak(k, f):
  def trig(x):
    return TrigBasis(k,x)
  def funcTrig(x):
    return TrigBasis(k,x)*f(x)
  return (1./ck(trig))*quad(funcTrig,-1,1)[0]

# generate trig poly of order k using the step fxn f
def P(k,f):
  def poly(x):
    res = 0
    for i in range(k+1):
      res += ak(k-i,f)*TrigBasis(k-i,x)
    return res
  return poly
