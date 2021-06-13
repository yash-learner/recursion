def nth_fibonacci(n):
    if n <= 1:
        return n
    else:
        return nth_fibonacci(n-1)+nth_fibonacci(n-2)


n = int(input())
print(nth_fibonacci(n))
