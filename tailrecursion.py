'''
  A recursion function is called as Tail Recursion when the last
  statement to be executed is a recursion call means there is no
  more statement to executed after the recursion call.

  Most modern compilers try to convert the non-tail recursive functions
  to tail recursive functions because they are fast when compared to
  non-tail recursive function calls

  In the Tail Recursive function  their is no need to store the state of the
  function call because there is no statement to executed after the call

  printing n to 1 is tail recursive but printing 1 to n is not tail recursive
'''


# TODO: NON-TAIL RECURSIVE FUNCTION
def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n*factorial(n-1)


n = int(input())
print(factorial(n))


# TODO: TAIL RECURSIVE FUNCTION
def tail_factorial(n, k):
    if n == 1 or n == 0:
        return k
    else:
        return tail_factorial(n-1, n*k)


n = int(input())
print(tail_factorial(n, 1))
