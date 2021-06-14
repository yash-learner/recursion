def rope_cut(n, a, b, c):
    if n == 0:
        return 0
    elif n < -1:
        return -1
    else:
        cuts = max(rope_cut(n-a, a, b, c), rope_cut(n -
                   b, a, b, c), rope_cut(n-c, a, b, c))

    if cuts == -1:
        return -1
    else:
        return cuts + 1


n, a, b, c = map(int, input().split())
print(rope_cut(n, a, b, c))


'''
  Time complexity : O(3^n)
  Space Complexity : O(n)
'''
