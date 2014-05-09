import matplotlib.pyplot as PLT
import eulersModified as em2
import eulersMethod as em1
import exactSolution as es
import rk4 as rk

# h = 0.2, actual
a1 = es.compute(11,0.2)
at1 = a1[0]
ax1 = a1[1]

# h = 0.1, actual
a2 = es.compute(21,0.1)
at2 = a2[0]
ax2 = a2[1]

# h = 0.05, actual
a3 = es.compute(41,0.05)
at3 = a3[0]
ax3 = a3[1]

# h = 0.2, rk4 
h1 = rk.rk4(False,10.0)
t1 = h1[0]
x1 = h1[1]

# h = 0.1, rk4
h2 = rk.rk4(False,20.0)
t2 = h2[0]
x2 = h2[1]

# h = 0.05, rk4
h3 = rk.rk4(False,40.0)
t3 = h3[0]
x3 = h3[1]

# h = 0.2, euler's method
h4 = em1.EulersMethod(False,10.0)
t4 = h4[0]
x4 = h4[1]

# h = 0.1, euler's method
h5 = em1.EulersMethod(False,20.0)
t5 = h5[0]
x5 = h5[1]

# h = 0.05, euler's method
h6 = em1.EulersMethod(False,40.0)
t6 = h6[0]
x6 = h6[1]

# h = 0.2, euler's modified
h7 = em2.EulersModified(False,10.0)
t7 = h7[0]
x7 = h7[1]

# h = 0.1, euler's modified
h8 = em2.EulersModified(False,20.0)
t8 = h8[0]
x8 = h8[1]

# h= 0.05, euler's modified
h9 = em2.EulersModified(False,40.0)
t9 = h9[0]
x9 = h9[1]

""""

# rk4
PLT.figure(1)
PLT.title("rk4 method")
PLT.plot(t1, x1, 'go-', label='h = 0.2')
PLT.plot(t2, x2, 'ro-', label='h = 0.1')
PLT.plot(t3, x3, 'bo-', label='h = 0.05')

# euler's method
PLT.figure(2)
PLT.title("euler's method")
PLT.plot(t4, x4, 'go-', label='h = 0.2')
PLT.plot(t5, x5, 'ro-', label='h = 0.1')
PLT.plot(t6, x6, 'bo-', label='h = 0.05')

# euler's modified method
PLT.figure(3)
PLT.title("euler's modified method")
PLT.plot(t7, x7, 'go-', label='h = 0.2')
PLT.plot(t8, x8, 'ro-', label='h = 0.1')
PLT.plot(t9, x9, 'bo-', label='h = 0.05')

"""

# h = 0.2
PLT.figure(1)
PLT.title("h = 0.2")
PLT.plot(t1,x1,'go-',label='rk4')
PLT.plot(t4,x4,'ro-',label='euler\'s method')
PLT.plot(t7,x7,'bo-',label='euler\'s modified method')
PLT.plot(at1,ax1,'mo-',label='actual')

"""

# h = 0.1
PLT.figure(1)
PLT.title("h = 0.1")
PLT.plot(t2,x2,'go-',label='rk4')
PLT.plot(t5,x5,'ro-',label='euler\'s method')
PLT.plot(t8,x8,'bo-',label='euler\'s modified method')
PLT.plot(at2,ax2,'mo-',label='actual')

# h = 0.05
PLT.figure(1)
PLT.title("h = 0.05")
PLT.plot(t3,x3,'go-',label='rk4')
PLT.plot(t6,x6,'ro-',label='euler\'s method')
PLT.plot(t9,x9,'bo-',label='euler\'s modified method')
PLT.plot(at3,ax3,'mo-',label='actual')

"""

# build graph
PLT.axis([0, 2, 0.3, 1])
PLT.legend()
PLT.show()