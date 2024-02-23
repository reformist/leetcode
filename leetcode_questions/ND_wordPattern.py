class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # general idea: map each letter in pattern to a word in array
        # a b b a would map to yes fish fish yes
        # but a b b c wouldn't work
        # need to check for two things: each letter must have the same word it's assigned
        # check that the two or more letters don't have the same value
        s_array = s.split(" ")

        if len(pattern) != len(s_array):
            return False

        matchDict = dict()

        for i in range(len(pattern)):
            if pattern[i] in matchDict:
                if matchDict[pattern[i]] != s_array[i]:
                    return False
            matchDict[pattern[i]] = s_array[i]
        
        if len(matchDict.keys()) != len(set(matchDict.values())):
            return False
        
        return True
