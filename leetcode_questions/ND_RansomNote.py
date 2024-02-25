# the problem 
# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

# Example 1:

# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:

# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:

# Input: ransomNote = "aa", magazine = "aab"
# Output: true

# general idea: create two dictionaries for both ransom note and magazine and then compare to ensure that every val in ransom note 
# can be found in magazine and that there are at least as many instances of letters in magazine as there are in ransom note
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        magazine_dict = dict()
        ransom_dict = dict()

        if len(ransomNote) > len(magazine):
            return False

        for i in ransomNote:
            if i in ransom_dict:
                ransom_dict[i] += 1
            else:
                ransom_dict[i] = 1
    
        for i in magazine:
            if i in magazine_dict:
                magazine_dict[i] += 1
            else:
                magazine_dict[i] = 1

        for i in ransom_dict:
            if i not in magazine_dict:
                return False
            elif ransom_dict[i] > magazine_dict[i]:
                return False
        
        return True

        
