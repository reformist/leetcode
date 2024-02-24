class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        diff_dict = {} # stores the difference between number and target

        for i in range(len(nums)):
            num = nums[i]

            if num in diff_dict.keys(): # then the number accomodates the difference
                num2_idx = diff_dict[num]
                return [num2_idx, i]
            
            diff = target - num
            diff_dict[diff] = i
