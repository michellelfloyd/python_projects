def exponent(base, exp, current_value=1):
    if exp == 0:
        return current_value
    current_value *= base
    exp -= 1

    return exponent(base, exp, current_value)

print exponent(5, 6)



def raising_to(base, exp):
    if exponent == 0:
        return 1
    return base * raising_to(base, exp -1)


print raising_to(2,3)