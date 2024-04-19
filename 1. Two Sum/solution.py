nums = [2,7,11,15]
target = 9

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict_indices_of_difference = {}
        for index,num in enumerate(nums):
            difference = target - num
            if difference in dict_indices_of_difference:
                return [dict_indices_of_difference[difference],index]
            dict_indices_of_difference[num] = index
            