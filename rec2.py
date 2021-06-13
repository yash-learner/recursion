def fun1(n):
    if n == 0:
        return
    else:
        print("GFG")
        fun1(n-1)


n = int(input())
fun1(n)
