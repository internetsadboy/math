from math import fabs

# actual - approximation / actual
def relativeError(a,b):
	return (a-b)/a

if False:
	print relativeError(3.0,2.0)

# relative-errors.txt for RK4, Euler's, Euler's Modified
with open("relative-errors.txt", "w") as io:
	io.write("RK4\n")
	io.write("h=0.2\n")
	io.write("t=1 "+str(fabs((0.419169104045 - 0.419270018285) / 0.419169104045))+"\n")
	io.write("t=2 "+str(fabs((0.772894528 - 0.772921871272) / 0.772894528))+"\n")
	io.write("h=0.1\n")
	io.write("t=1 "+str(fabs((0.419169104045 - 0.419174435538) / 0.419169104045))+"\n")
	io.write("t=2 "+str(fabs((0.772894528 - 0.772895991712) / 0.772894528))+"\n")
	io.write("h=0.05\n")
	io.write("t=1 "+str(fabs((0.419169104045 - 0.419169410527) / 0.419169104045))+"\n")
	io.write("t=2 "+str(fabs((0.772894528 - 0.772894631567) / 0.772894528))+"\n")
	io.write("Euler's Modified Method\n")
	io.write("h=0.2\n")
	io.write("t=1 "+str(fabs((0.419169104045 -  0.431741696) / 0.419169104045))+"\n")
	io.write("t=2 "+str(fabs((0.772894528 - 0.776424035252) / 0.772894528))+"\n")
	io.write("h=0.1\n")
	io.write("t=1 "+str(fabs((0.419169104045 - 0.42181003917) / 0.419169104045))+"\n")
	io.write("t=2 "+str(fabs((0.772894528 - 0.773614951648) / 0.772894528))+"\n")
	io.write("h=0.05\n")
	io.write("t=1 "+str(fabs((0.419169104045 - 0.419778071878) / 0.419169104045))+"\n")
	io.write("t=2 "+str(fabs((0.772894528 - 0.773059674952) / 0.772894528))+"\n")
	io.write("Euler's Method\n")
	io.write("h=0.2\n")
	io.write("t=1 "+str(fabs((0.419169104045 - 0.3472) / 0.419169104045))+"\n")
	io.write("t=2 "+str(fabs((0.772894528 - 0.757558272) / 0.772894528))+"\n")
	io.write("h=0.1\n")
	io.write("t=1 "+str(fabs((0.419169104045 - 0.384217728) / 0.419169104045))+"\n")
	io.write("t=2 "+str(fabs((0.772894528 - 0.764411518808) / 0.772894528))+"\n")
	io.write("h=0.05\n")
	io.write("t=1 "+str(fabs((0.419169104045 - 0.401970818238) / 0.419169104045))+"\n")
	io.write("t=2 "+str(fabs((0.772894528 - 0.768476103677) / 0.772894528))+"\n")


