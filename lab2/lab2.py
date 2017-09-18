from task1 import BuildMatrix
from task2 import Summmmm
def main():
	print("task1")
	BuildMatrix()
	print("\ntask2")
	n = int(input("input n: "))
	x = float(input("input x: "))
	y = []
	for i in  range(0,n):
		y.append(float(input("y["+str(i+1)+"] = ")))
	print(Summmmm(y,x))
main()