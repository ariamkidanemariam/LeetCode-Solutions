class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in nums:
                j = nums.index(complement)

                if j != i:
                    return [i, j]