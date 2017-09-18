def task1():
	x = float(input("input X: \n"))
	e = float(input("input e: \n"))
	i = 1
	previous_a = x
	current_a = 1/3 * ( previous_a + x*x / previous_a)
	while  abs(current_a - previous_a) > e:
		previous_a = current_a
		current_a = 1/3 * (previous_a + x*x/previous_a)
		i += 1
	return "a = " + str(current_a) + ", n = " + str(i)
