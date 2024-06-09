class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        
        # largest str s.t. x divides str 1 and str2

        # test each char
        # if not even one char divides, then nothing divides

        x = ''

        # try all prefixes

        # need to confirm 2 things
        # 1. is it a divisor of str1
        # AND is it also one for str2

        min_len = min(len(str1), len(str2))

        # 

        for i in range(min_len):
            prefix = str2[:i+1] 

            if self.check_division(prefix, str1) and self.check_division(prefix, str2):
                x = prefix
        
        return x
            
    def check_division(self, sub_str, big_str):
        new = ''

        while len(new) <= len(big_str):
            if new == big_str: # confirms it divides at some point
                return True
            new += sub_str

        return False
