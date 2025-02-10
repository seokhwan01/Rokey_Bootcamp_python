arr=[21,10,11,15,13]
for i in range(len(arr)-1):
    min=arr[i]
    index=i
    for j in range(i+1,len(arr)):
        if arr[j]<min:
            min=arr[j]
            index=j
    arr[i],arr[index]=arr[index],arr[i]
print(arr)