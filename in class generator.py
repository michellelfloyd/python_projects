def primes():
    i = 1

    while True:

        for divisor in range(i/2, i):
            if i % divisor == 0:
                i += 1

                break
        else:
            yield i
            i += 1

prime_gen = primes()


print prime_gen.next()
print prime_gen.next()
print prime_gen.next()
print prime_gen.next()