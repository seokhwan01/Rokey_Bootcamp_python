# a = [10, 20, 30]
# b = a.copy()
# print(f"a: {id(a)}, b : {id(b)}")

def total_dic(dic):
    total=0
    for i in dic.values():
        total+=i
    return total
dic = { 'a': 10, 'b': 20, 'c': 30 }
print(total_dic(dic))
    
