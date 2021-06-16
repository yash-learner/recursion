def josephus_problem(n, k):
    if n == 1:
        return 0
    else:
        return (josephus_problem(n-1, k)+k) % n


n, k = map(int, input().split())
print(josephus_problem(n, k))


'''
    In recursion always build for small cases
    build solution for n-1 and then find n using n-1

    Time Complexity : O(n)
    Space Complexity : O(n)

    whenever looking for the position between 0 to n - 1
    do modulo
'''
