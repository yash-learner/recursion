# TODO: NON-TAIL RECURSIVE SOLUTION
def sum_of_natural_numbers(n):
    if n == 1:
        return 1
    else:
        return n+sum_of_natural_numbers(n-1)


n = int(input())
print(sum_of_natural_numbers(n))

# TODO: TAIL RECURSIVE SOLUTION


def tailrecursive_sum_of_natural_numbers(n, k):
    if n == 1:
        return k
    else:
        return tailrecursive_sum_of_natural_numbers(n-1, n+k)


n = int(input())
print(tailrecursive_sum_of_natural_numbers(n, 1))


'''
  T.C = O(n) => T(n) = T(n-1)+THETA(1)
  here T(n-1) are recursive calls and THETA(1) is the work done by each call
  S.C = O(n)
'''
