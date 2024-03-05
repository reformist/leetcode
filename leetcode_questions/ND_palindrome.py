# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.


# general idea: starting from left and moving to the right, compare elements in the string.
# if the string differes at any elements you know it's not a palindrome
# the problem is filtering the string for only alphanumeric characters, which you can do useing the re module.

import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0: return True
        # start two pointers from both ends and then compare
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        s = s.lower()
        
        left_pointer = 0
        right_pointer = len(s) - 1

        print(s)

        while left_pointer < right_pointer:
            if s[left_pointer] != s[right_pointer]:
                return False
            left_pointer += 1
            right_pointer -=1 

        return True

        
        
