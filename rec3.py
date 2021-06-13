def rec3(n):
    if n == 0:
        return
    else:
        print(n)
        rec3(n-1)
        print(n)


n = int(input())
rec3(n)
