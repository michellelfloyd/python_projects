from time import clock


def naive_fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return naive_fib(n-1) + naive_fib(n-2)


def fib_helper(n):
    if n == 0:
        return 0
    else:
        return fib_improved(n, 0, 1)


def fib_improved(n, p0, p1):
    if n == 1:
        return p1
    else:
        return fib_improved(n-1, p1, p0 + p1)


for i in range(0, 41):
    n = i
    start = clock()
    result = naive_fib(n)
    stop = clock()
    difference = (stop - start) * 1000  # clock returns a value in seconds.

    start1 = clock()
    result1 = fib_helper(n)
    stop1 = clock()
    difference1 = (stop1 - start1) * 1000  # clock returns a value in seconds.

    print "naive_fib("+str(n)+") =" + str(result) + " taking " + str(difference), "ms"
    print "fib_helper("+str(n)+") =" + str(result1) + " taking " + str(difference1), "ms"




