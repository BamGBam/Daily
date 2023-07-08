class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Tools Array, List, 
        list = []
        count = 0
        # for i in range(len(nums)):
        #     if nums[i] ==  i:
        #             count += 1
        counts = dict()
        for i in nums:
            counts[i] = counts.get(i, 0) + 1
        highest = max(counts, key = counts.get)
        print(highest)
        return counts

sol = Solution()

# Call the singleNumber method on the instance
result = sol.singleNumber([3, 4, 4, 3, 3,3,3])
print(result)