def mergesort(arr,l,h):
    c=0
    m=(l+h)//2
    if l<h:
        c+=mergesort(arr,l,m)
        c+=mergesort(arr,m+1,h)
        i=l
        j=m+1
        temp=[]
        while(i<=m and j<=h):
            if arr[i]>arr[j]:
                c+=h-l+1
                temp.append(arr[j])
                j+=1
            else:
                temp.append(arr[i])
                i+=1
        while(i<=m):
            temp.append(arr[i])
            i+=1
        while(j<=h):
            temp.append(arr[j])
            j+=1
        for i in range(l,h+1):
            arr[i]=temp[i-l]
    return c
arr=[2,1]
ans=mergesort(arr,0,len(arr)-1)
print(ans)