def generate_subsets(s, curr, index):
    if index == len(s):
        print(curr)
        return
    else:
        generate_subsets(s, curr, index+1)
        generate_subsets(s, curr+s[index], index+1)


s = input()
generate_subsets(s, "", 0)

'''
    Time Complexity : O(n)
    Space Complexity : O(n)
'''
