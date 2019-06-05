print " Life is hard. There are 4 doors:"

door = raw_input("> ")

if door == "1":
	print "boring"

elif door == "2" or "3":
	print "but why?"
	response = raw_input("> ")
	print response * int(door)
	
else:
	print "failure"
