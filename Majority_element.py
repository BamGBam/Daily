class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        highest = 0
        number = 0
        for i in range(len(nums)):
            count = nums.count(nums[i])
            if count > highest:
                highest = count 
                number = nums[i]
        if highest > (abs(len(nums) / 2)):
            return number
        return -1

sol = Solution()

# Call the singleNumber method on the instance
result = sol.singleNumber([2, 4,4, 4,4,4, 2, 2])
print(result)