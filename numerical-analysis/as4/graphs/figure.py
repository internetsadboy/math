from matplotlib.pyplot import *

# h = 0.2 graph
# h = 0.1 graph
# h = 0.05 graph
# (t,x) Euler,Euler-Modified,RK4
plot([0.0,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.8], [0.41,0.28,0.36,0.44,0.5,0.6,0.7,0.8,0.9,1.0], 'ro-',  label='line 2')

axis([0, 2, 0, 1])
legend()
show()

"""
plt.figure(1)
plt.title('eqn1-eqn2 and the single dimension approximation')

plt.figure(2)
plt.title('eqn1 and eqn2 with the two dimensional approximation')"""