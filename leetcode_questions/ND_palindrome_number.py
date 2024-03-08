# given integer, how to determine if it's a palindrome or not?
# convert to string, two pointers

class Solution:
    def isPalindrome(self, x: int) -> bool:
        string_x = str(x)

        right_pointer = len(string_x) - 1
        left_pointer = 0

        while right_pointer > left_pointer:
            if string_x[right_pointer] != string_x[left_pointer]:
                return False
            right_pointer-=1
            left_pointer +=1
        
        return True
        
