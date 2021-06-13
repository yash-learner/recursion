def print_nto1(n):
    if n == 0:
        return
    else:
        print(n)
        print_nto1(n-1)


n = int(input())
print_nto1(n)
