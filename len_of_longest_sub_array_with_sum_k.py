def lenOfLongSubarr (arr, n, k) :
        pre={}
        s=0
        l=0
        for i in range(n):
            s+=arr[i]
            if s==k:
                l=max(l,i+1)
            if s-k in pre:
                l=max(l,i-pre[s-k])
            pre[s]=i
        return l
arr=[1,2,-2,-1]
target=0
print(lenOfLongSubarr(arr,len(arr),target))