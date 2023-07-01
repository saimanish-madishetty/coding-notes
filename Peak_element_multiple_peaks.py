class Solution(object):
    def findPeakElement(self, nums):
        n=len(nums)
        if n==1:
            return 0
        if nums[0]>nums[1]:
            return 0
        if nums[n-1]>nums[n-2]:
            return n-1
        l=1
        h=n-2
        while(l<=h):
            m=(l+h)//2
            if nums[m-1]<nums[m]>nums[m+1]:
                return m
            elif nums[m-1]<nums[m]:
                l=m+1
            else:
                h=m-1
        return -1
obj = Solution()
arr=[1,2,1,-1,0,-2]
print(obj.findPeakElement(arr))