f=open("C:\\rokey\\ch12\\file1.txt",'w',encoding="utf-8")
for i in range(1,11):
    data="%d번째 줄입니다.\n" % i
    f.write(data)
f.close()