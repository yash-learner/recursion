
def tower_of_hanoi(n, A, B, C):

    if n == 1:
        print(" Move "+"1"+" from "+A+" to "+C)
        return
    else:
        tower_of_hanoi(n-1, A, C, B)
        print(" Move {} from {} to {}".format(n, A, C))
        tower_of_hanoi(n-1, B, A, C)


n = int(input())
tower_of_hanoi(n, "A", "B", "C")


"""
    Time Complexity : O(2^n)
    Space Complexity : O(n)
"""
