ca=[21,10,11,15,13]

for i in range(len(ca)):
    min=ca[i]
    index=i
    for j in range(i+1,len(ca)):
        if ca[j]<min:
            min=ca[j]
            index=j
    #첫번째 요소와 최솟값 자리 교체
    ca[i],ca[index]=ca[index],ca[i]
print(ca)
