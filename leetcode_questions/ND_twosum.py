class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # brief explanation: think about complement and doing this in one pass. keys in newdict are the values in nums and the indices are the 
        # values in newdict. for every value in nums, iterate and find the complement. if the complement is in newdict keys, return the
        # indices of the complement and of the current i in nums. if not, add the value in nums as a key to newdict. this prevents counting 
        # the same index twice.
        newdict = dict()
        
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in newdict:
                return [newdict[complement], i]
            newdict[nums[i]] = i


        
