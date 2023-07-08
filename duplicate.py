class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Maybe using hashmap
        lst = nums[:]
        for i in range(len(lst)):
            if(nums[i] in lst):
                lst.remove(nums[i])
                print(lst)
                if nums[i] not in lst:
                    return nums[i]


# Create an instance of the Solution class
Solution = Solution()

# Call the singleNumber() method on the instance, passing the list as an argument
result = Solution.singleNumber([2,2,1,1,1,2,2])
print(result)
