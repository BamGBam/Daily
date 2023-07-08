class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Maybe using hashmap
        lst = []
        count = len(nums)
        for i in range(len(nums)):
            if nums[i] != 0:
                lst.append(nums[i])
                count -= 1
        print("count is", count)
        while(count):
            lst.append(0)
            count -= 1
        print("list is", lst)
        return lst


# Create an instance of the Solution class
Solution = Solution()

# Call the singleNumber() method on the instance, passing the list as an argument
result = Solution.singleNumber([0,1,0,3,12, 0])
print(result)
