
from array import array

# Create an array for the counters.
zeros = [0 for x in range(127)]


theCounters = array( 'i', zeros )

# for i in range(len(theCounters)):
#     theCounters[i]=0
# print len(theCounters)

# Open the text file for reading and extract each letter.

theFile = open( 'project_5.py', 'r' )

for line in theFile :

    for letter in line :

        code = ord( letter )

        theCounters[code] += 1

# Close the file

theFile.close()

# Print the results.

for i in range( 26 ) :

    print( "%c - %4d %c - %4d" % \

    (chr(65+i), theCounters[65+i], chr(97+i), theCounters[97+i]) )