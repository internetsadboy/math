def polyLeastSquares(n,X,Y):
  polynomials = []
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
    poly.append(yx)
    polynomials.append(poly)
  print polynomials[0]
  print polynomials[1]
  print polynomials[2]

# example pg 502
polyLeastSquares(2,[0,0.25,0.5,0.75,1],[1.0000,1.2840,1.6487,2.1170,2.7183])
# output
# [5.0, 2.5, 1.875, 8.768]
# [2.5, 1.875, 1.5625, 5.4514000000000005]
# [1.875, 1.5625, 1.3828125, 4.4015375]
