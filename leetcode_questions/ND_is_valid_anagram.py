class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool        """

            
        if len(s) != len(t):
            return False
        dict1 = dict()
        dict2 = dict()
        
        for i in range(len(s)):
            if s[i] not in dict1.keys():
                dict1[s[i]] =1
            else:
                dict1[s[i]] += 1
            # how to create a key
        for i in range(len(t)):
            if t[i] not in dict2.keys():
                dict2[t[i]] =1
            else:
                dict2[t[i]] += 1

        for key in dict1.keys():
            print(dict1)
            if (key in dict2.keys()) and (dict1[key] == dict2[key]):
                continue
            else:
                return False

        return True        


         
   
