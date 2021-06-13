def rec5(n):
    if n == 1:
        return 0
    else:
        return 1 + rec5(n//2)


n = int(input())
print(rec5(n))

''''
the answer is floor of logn ^ 2

the answer is 4 for all the numbers between 16 and 31 and for 32 to 63 it is 5

if the divisor is 3 then then the answer is logn ^ 3 and base condition will be n < 3
'''
