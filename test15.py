#from sys module, imports argv function
from sys import argv

# pulls from command line specification
script, filename = argv

# creates object from filepath
txt = open(filename)

# reads object created above
print "Here's your file %r:" % filename
print txt.read()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()

txt.close()
txt_again.close()
