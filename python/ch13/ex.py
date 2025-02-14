# while True:
#     try:
#         x = int(input("Please enter a number: "))
#         break
#     except ValueError:
#         print("Oops! That was no valid number. Try again...")
# try: 
#     f = open('myfile.txt') 
#     s = f.readline() • i = int(s.strip()) 
# except OSError as err: 
#     print("OS error:", err) 
# except ValueError: 
#     print("Could not convert data to an integer.") 
# except Exception as err: 
#     print(f"Unexpected {err=}, {type(err)=}")

# try: 
#     raise NameError('HiThere') 
# except NameError:
#     print('An exception flew by!')

# my_list=["010","9274","0795"]
# phone="-".join(my_list)
# print(phone)
numbers=[1,2,3]
squared_numbers=map(lambda x : x**2,numbers)
print(list(squared_numbers))