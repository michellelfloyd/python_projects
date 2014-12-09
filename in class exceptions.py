def fileOpen(self, file):
    open(file)



def fileOpenAgain(self):

    try:
        open("non_existent_file.txt")
    except IOError:
        print "Error: can\'t find file or read data"

try:
    fileOpen(1, "non_existent_file.txt")
except:
    print "Error: can\'t find file or read data"

fileOpenAgain(1)
