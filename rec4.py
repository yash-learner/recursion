def rec4(n):
    if n == 0:
        return
    else:
        rec4(n-1)
        print(n)
        rec4(n-1)


n = int(input())
# print(rec4(n))
rec4(n)


'''

rec(3)
   rec(2)
       rec(1)
           rec(0)
               return
            1
            rec(0)
               return
    2
    rec(1)
       rec(0)
           return
        1
        rec(0)
           return

3
rec(2)
  rec(1)
    rec(0)
      return
    1
    rec(0)
      return
  2
  rec(1)
    rec(0)
      return
    1
    rec(0)
     return


'''
