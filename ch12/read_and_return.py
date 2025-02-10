# path="C:\\rokey\\ch12\\file1.txt"
# mode="r"
# arr=[]
# with open(path,mode,encoding="utf-8") as f:
#     lines=f.readlines()
#     for line in lines:
#         arr.append(line.split()[1])
#     print(arr)
# f=open(path,'r',encoding="utf-8")
# lines=f.readlines()
# list=[]
# for line in lines:
#     #print(line,end="")
#     list.append(line.split()[1])
# print(list)
# f.close()

# path="C:\\rokey\\ch12\\file1.txt"
# mode="a"
# data="강호동 147-12-002093\n유재석 146-22-102093"
# with open(path,mode,encoding="utf-8") as f:
#     f.write(data)
    
# mode="r"
# arr=[]
# with open(path,mode,encoding="utf-8") as f:
#     lines=f.readlines()
#     for line in lines:
#         arr.append(line.split()[1])
#     print(arr)

path="C:\\rokey\\ch12\\file1.txt"
mode="r"
dic={}
with open(path,mode,encoding="utf-8") as f:
    lines=f.readlines()
    for line in lines:
        linelist=line.split(" ")
        dic[linelist[0]]= linelist[1]
print(dic)