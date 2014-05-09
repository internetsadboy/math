from math import exp as e

# x(t) = (5/4)*(e^-2*t) + (1/4)*(2*t-1)
# exactSolution(1) => 0.419169104046
# exactSolution(2) => 0.772894548611
def exactSolution(t):
	return 1.25*e(-2*t)+0.25*(2*t - 1)

def compute(n,h):
	t = 0.0
	D = []
	T = []
	X = []
	fileName = "h"+str(n-1)+".txt"
	with open(fileName, "w") as io:
		for k in range(n):
			x = exactSolution(t)
			X.append(x)
			if len(str(t)) == 3:
				io.write(str(t)+" ".ljust(2)+str(x)+"\n")	
			else:
				io.write(str(t)+" "+str(x)+"\n")
			T.append(t)
			t+=h
		D.append(T)
		D.append(X)
		return D
	
# test compute(11,0.2)