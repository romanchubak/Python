def InitMatrix(n,m):
	X = []
	for i in range(0,n):
		X.append([])
		for j in range(0,m):
			X[i].append(0)
	return X

def scalar(vec1, vec2):
	sum = 0
	if len(vec1) != len(vec2):
		return -1
	else:
		for i in range(0,len(vec1)):
			sum += vec1[i] * vec2[i]
		return sum

def BuildMatrix():
	n=int(input("input n: "))
	X = InitMatrix(n,n)
	Y = InitMatrix(n,n)
	for i in range(0,n):
		print("input "+str(i+1) + "row")
		for j in range(0,n):
			X[i][j] = int(input("X["+str(i+1)+"]["+str(j+1)+"] =" ))
	
	for i in range(0,n):
		for j in range(0,n):
			vec_i = X[i]
			vec_j = []
			for k in range(0,n):
				vec_j.append(X[k][j])
			Y[i][j] = scalar(vec_i,vec_j)	
	print("Y = ")
	for i in range(0,n):
		print(Y[i])
