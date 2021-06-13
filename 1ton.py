def print_1ton(n):
    if n == 0:
        return
    else:
        print_1ton(n-1)
        print(n)


n = int(input())
print_1ton(n)
