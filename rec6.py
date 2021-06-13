def rec6(n):
    if n == 0:
        return
    rec6(n//2)
    print(n % 2)


n = int(input())
rec6(n)
