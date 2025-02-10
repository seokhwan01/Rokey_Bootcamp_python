path="C:\\rokey\\ch12\\file1.txt"
f=open(path,'r',encoding="utf-8")
line=f.readline()
print(line)
f.close()