#def sum_list(l):
 #   """"returns the sums of the contents of a list of numbers """
 #   sum = 0
 #   for i in l:
  #      sum += i
 #   return sum


def sum_list(l):
    if not l:
        return 0

    return l.pop() + sum_list(l)

print sum_list([4, 6, 3, 6, 7, 4, 3, 8])
