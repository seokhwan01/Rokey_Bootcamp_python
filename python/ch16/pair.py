def pair_test(arr):
    pair=[]
    for i in arr:
        if i=='(':
            pair.append('(')
        elif i==')':
            if pair.pop()=='(':
                pass
            else:
                return False
            
        elif i=='[':
            pair.append('[')
        elif i==']':
            if pair.pop()=='[':
                pass
            else:
                return False
            
            
        elif i=='{':
            pair.append('{')
        elif i=='}':
            if pair.pop()=='{':
                pass
            else:
                return False
    return True
input_str=input("문자열 입력  : ")
print(pair_test(input_str))

        