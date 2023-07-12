def countOfArray(arr):
    mx=float('-inf')
    c=0
    for i in range(len(arr)):
        if arr[i]>mx:
            mx=arr[i]
    for i in range(len(arr)):
        if arr[i]==mx:
            c+=1
    return len(arr)-c

arr=list(map(int,input().split()))
print(countOfArray(arr))