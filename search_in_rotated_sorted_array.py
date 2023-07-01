class Solution(object):
    def bs(self,arr,x):
        l=0
        h=len(arr)-1
        while(l<=h):
            m=(l+h)//2
            if arr[m]==x:
                return m
            elif arr[m]<x:
                l=m+1
            else:
                h=m-1
        return -1
    def search(self, arr, x):
        l=0
        h=len(arr)-1
        idx=-1
        while(l<=h):
                m=(l+h)//2
                if arr[m]>arr[-1]:
                    idx=m
                    l=m+1
                else:
                    h=m-1
        arr1=arr[:idx+1]
        arr2=arr[idx+1:]
        res1=self.bs(arr1,x)
        res2=self.bs(arr2,x)
        if res1==-1 and res2==-1:
            return -1
        if res1!=-1 and res2==-1:
            return res1
        if res1==-1 and res2!=-1:
            return res2+len(arr1)
obj = Solution()
arr=[6,7,8,9,10,1,2,3,4,5]
print(obj.search(arr,5))