def check_palindrome(s, start, end):
    if start >= end:
        return True
    elif s[start] == s[end]:
        return check_palindrome(s, start+1, end-1)
    else:
        return False


string = input()
print(check_palindrome(string, 0, len(string)-1))


'''
  Time Complexity: O(n) => T(n) = T(n-2)+THETA(1)
  Space Complexity: O(n)
  we consider empty string and single character as palindrome
'''
