def T(n,x):
	if n == 0:
		return 1
	if n == 1:
		return x
	if n==2:
		return 2*x*x - 1
	else:
		return 2*x*T(n-1,x) - T(n-2,x)
def Summmmm(y,x):
	sum = 0
	for i in range(0,len(y)):
		sum += (-y[i])**i * T(i,x)
	return sum