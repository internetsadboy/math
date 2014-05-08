import matplotlib.pyplot as PLT
import eulersMethod as em1
import eulersModified as em2
import rk4 as rk

# h = 0.2, rk4 
rk.rk4(False,10.0)
t1 = rk.getT()
x1 = rk.getX()

# h = 0.2, euler's method
em1.EulersMethod(False,10.0)
t2 = em1.getT()
x2 = em1.getX()

# h = 0.2, euler's modified
em2.EulersModified(False,10.0)
t3 = em2.getT()
x3 = em2.getX()

# h = 0.1, rk4
rk.rk4(False,20.0)
t4 = rk.getT()
x4 = rk.getX()

# h = 0.1, euler's method
em1.EulersMethod(False,20.0)
t5 = em1.getT()
x5 = em1.getX()

# h = 0.1, euler's modified
em2.EulersModified(True,20.0)
t6 = em2.getT()
x6 = em2.getX()

# h = 0.05, rk4
rk.rk4(False,40.0)
t7 = rk.getT()
x7 = rk.getX()

# h = 0.05, euler's method
em1.EulersMethod(False,40.0)
t8 = em1.getT()
x8 = em1.getX()

# h= 0.05, euler's modified
em2.EulersModified(False,40.0)
t9 = em2.getT()
x9 = em2.getX()

fig = PLT.figure()

# h = 0.2 graph
PLT.figure(1)
PLT.title("where h = 0.2")
PLT.plot(t1, x1, 'go-', label='rk4')
PLT.plot(t2, x2, 'ro-', label='euler\'s method')
PLT.plot(t3, x3, 'bo-', label='euler\'s modified')

# h = 0.1 graph
PLT.figure(2)
PLT.title("where h = 0.1")
PLT.plot(t4, x4, 'go-', label='rk4')
PLT.plot(t5, x5, 'ro-', label='euler\'s method')
PLT.plot(t6, x6, 'bo-', label='euler\'s modified')

# h = 0.05 graph
PLT.figure(3)
PLT.title("where h = 0.05")
PLT.plot(t7, x7, 'go-', label='rk4')
PLT.plot(t8, x8, 'ro-', label='euler\'s method')
PLT.plot(t9, x9, 'bo-', label='euler\'s modified')

# build graph
PLT.axis([0, 2, 0, 1])
PLT.legend()
PLT.show()