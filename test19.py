def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % (cheese_count ** 2)
	print "You have %d boxes of crackers!" % (boxes_of_crackers ** 2)
	print "Get a blanket.\n"
	
print "We can just give the function numbers directly:"
cheese_and_crackers(20,30)

print "OR, we can use variables from out script:"
amount_of_cheese = int(raw_input())
amount_of_crackers = int(raw_input())

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)