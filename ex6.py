# basic sentence adding format variable for 10
x = "There are %d types of people." % 10
# refs for below sentence
binary = "binary"
do_not = "don't"
# builds sentence around two above variables, same call %s
y = "Those who know %s and those who %s." % (binary, do_not)

# print component sentences with format variables
print x
print y

# x sentence with format is now formatted into below, same with y
print "I said: %r." % x
print "I also said: '%s'." % y

# simple variable defined
hilarious = False
# format built into sentence
joke_evaluation = "Isn't that joke so funny?! %r"

# string joined with variable defined above as basis for format
print joke_evaluation % hilarious

#define two strings
w = "This is the left side of ..."
e = "a string with a right side."

#show addition of strings
print w + e