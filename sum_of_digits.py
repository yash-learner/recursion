# TODO: TAIL RECURSIVE SOLUTION
def sum_of_digits(n, s):
    if n == 0:
        return s
    else:
        return sum_of_digits(n//10, s+n % 10)


n = int(input())
print(sum_of_digits(n, 0))


# print(245//10) => removes the last digit
# print(245 % 10) => gets the last digit

'''
  Time Complexity : O(len(n))
  Space Complexity : O(n)
'''


def ntr_sum_of_digits(n):
    if n == 0:  # n < 9
        return 0
    else:
        return n % 10+ntr_sum_of_digits(n//10)


n = int(input())
print(ntr_sum_of_digits(n))
