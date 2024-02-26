class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # # map each char to another
        # if len(s) != len(t):
        #     return False
        # if len(set(s)) != len(set(t)):
        #     return False
        
        # iso_dict = {}
        # for i in range(len(s)):
        #     if s[i] not in iso_dict.keys():
        #         iso_dict[s[i]] = t[i]
                
        #     elif iso_dict[s[i]] != t[i]:
        #         return False
        

        # return True



        # letters are isomorphic if letters in s can be replaced to get t
        # Isomorophic Strings
        # Given two strings s and t, determine if they are isomorphic.

        # Two strings s and t are isomorphic if the characters in s can be replaced to get t.

        # All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

        

        # Example 1:

        # Input: s = "egg", t = "add"
        # Output: true
        # Example 2:

        # Input: s = "foo", t = "bar"
        # Output: false
        # Example 3:

        # Input: s = "paper", t = "title"
        # Output: true

        # the general idea is to first check to see if lengths are equal and then make sure that the number 
        # of unique characters in each set is the same. if s or t has more characters than one another
        # can't replace them
        # then, we need to use a dictionary to ensure each char in s is mapped to one and only unique val in t
        # this is a one pass solution because I compare to t as I go
        if len(s) != len(t):
            return False
        if len(set(s)) != len(set(t)):
            return False
    
        s_dict = dict()


        for i in range(len(s)):
            if s[i] not in s_dict:
                s_dict[s[i]] = t[i]

            elif s_dict[s[i]] != t[i]:
                return False
        
        return True

        
