try:
    x = int(raw_input("Please enter your first integer: "))
except:
    x = int(raw_input("Please enter an integer:"))
try:
    y = int(raw_input("Please enter your second integer:"))
except:
    y = int(raw_input("Please enter an integer:"))
print "The sum of", x, "and", y, "is:",  x + y
print "The result of subtracting", y, "from", x, "is:", x - y
print "The product of", x, "and", y, "is:", x * y
print "The quotient of", x, "divided by", y, "is:", x / y, "with a remainder of:", x % y






