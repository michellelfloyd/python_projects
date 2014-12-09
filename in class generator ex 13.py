def frange(start, stop, increment):
        while start < stop:

            yield start
            start += increment

for n in frange(0, 4, 0.5):
    print n

x = frange(0, 7, 0.75)

y = frange(0, 10000, 250)

# while True:
#     print x.next()
#     print y.next()
