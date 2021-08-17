class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ##Corner case:Array has 0 or 1 element
        if(n==0 or n==1):
            return n

        j=1
        for i in range(1,n):
            if(nums[i]!=nums[i-1]):
                nums[j]=nums[i]
                j+=1
        return j