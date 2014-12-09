
f = open("project_seven.dat", "w")

print "**********************"
print "Project 7 Menu"
print "**********************"
print "1. Write input to file"
print "2. Write input to screen"
print "3. Quit"

while input != "3":
    input = raw_input("Enter your choice [1-3]:")
    if input == "1":
        input1 = raw_input("Enter a phrase:")
        f.write(input1)
    elif input == "2":
        input2 = raw_input("Enter a phrase:")
        print input2
print "This program will now quit"