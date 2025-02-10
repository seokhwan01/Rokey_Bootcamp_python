score = int(input("score : "))
grade=""

if 81<=score<=100 : 
    grade = "A"
elif 61<=score<=80:
    grade="B"
elif 41<=score<=60:
    grade="C"
elif 21<=score<=40:
    grade="D"
else :
    grade="E"
print(f"gade is {grade}")