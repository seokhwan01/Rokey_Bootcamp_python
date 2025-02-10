# with open("test.txt", "a") as file:
#     file.write("Hello, World!")
# print(file.closed)


# file = open("data.txt", "w")
# file.write("Python")
# file.close()
# file = open("data.txt", "r")
# print(file.read())
# file.close()
# print(file.close)

path="C:\\rokey\\ch12\\pizza_file1.txt"
mode="w"
with open(path,mode,encoding="utf-8") as f:
    f.write("페페로니 피자 3200\n치즈 피자 3200\n콤비네이션 피자 3500\n")
mode="a"
with open(path,mode,encoding="utf-8") as f:
    f.write("불고기 피자 3600\n해산물 피자 3800\n")
    
mode="r"
with open(path,mode,encoding="utf-8") as f:
    print(f.read())