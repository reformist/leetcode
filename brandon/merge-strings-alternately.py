class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """

        final_str = ""

        # iterate to the min of two str
        min_len = min(len(word1), len(word2))

        for i in range(min_len):
            final_str += word1[i]
            final_str += word2[i]

        if len(word1) > len(word2):
            final_str += word1[i+1:]
        else:
            final_str += word2[i+1:]

        return ''.join(final_str)
