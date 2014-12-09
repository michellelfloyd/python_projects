import string
import random


f = open("project_six.dat", "w")


def random_string(size=50, chars=string.ascii_letters + string.digits):
    final_string = ''
    for num in range(size):
        random_char = random.choice(chars)
        final_string += random_char
    f.write(final_string + "\n")


def generate_strings():
    for x in range(0, 10):
        random_string()


generate_strings()


cars = {}

f = open("project_six.dat", "r")
for line in f:
    cleaned_line = line.replace("\n", "")
    print "******* Begin Random String *******"
    print cleaned_line
    for char in cleaned_line:
        if char in cars:
            cars[char] += 1
        else:
            cars[char] = 1

    # build final count string
    final_count = ''
    for key in cars:
        final_count += "%s ==> %s; " % (key, cars[key])
    print final_count
    print"***********************************"
    cars = {}


f.close()
