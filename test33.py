def rep_numbers(halt,x):
	i = 0 
	numbers = []
	for i in range(0, halt +1):
		print "At the top i is %d" % i
		numbers.append(i)
	
		i = i + x
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i
	
	print "The numbers: "

	for num in numbers:
		print num