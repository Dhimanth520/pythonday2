# EXCEPTION HANDELING

# try:
#     a=int(input("Enter the value of a: "))
#     b=int(input("Enter the valure of b: "))
#     c=a/b
# except Exception as e:
#     print("Zero cannot be divided ",e)

# else: 
#     print("Successful execution",c)

# finally:
#     print("program completed")

# try:
#     while(True):
#         num=int(input("Enter the number: "))
#         if num>=0:
#             res=num*num
#             print("Square of the number is ",res)
#         else:
#             raise ValueError
# except ValueError as e:
#     print("The number is negative ",e)

# try:
#     num1=int(input("Enter the fst number:  "))
#     num2=int(input("Enter the sec number:  "))
#     res=num1/num2
#     print("The result is ",res)
# except Exception as e:
#     print("Cannot divide by zero ",e)
# import math
# try:
#     num=int(input("Enter the number: "))
#     if num<=0:
#         raise Exception("Enter a positive number")
#     else:
#         sqt=math.sqrt(num)
#         print("Square root of the number is ",sqt)
# except Exception as e:
#     print("the error is...",e)   


# dict1={"name":"dhim","age":23,"add":"bang"}
# print(dict1)
# try:
#     key=input("Enter the key: ")
#     if key in dict1:
#         print("The value of the key is ",dict1[key])

#     else:
#         raise Exception("Key noy found")
# except Exception as e:
#     print("the error is...",e)            
# dict1={}
# try:
#     for i in range (3):
#         key=int(input("Enter the number(key): "))
#         if key<3:
#             raise Exception("The (key)number is less than 3: NmberTooSmal.... ")
#         value=int(input("Enter the value(cubes): "))
#         if value>30:
#             raise Exception("The value is greater than 20: ValueTooBig.... ")
#         dict1[key]=value
#     print(dict1)
# except Exception as e:
#     print("there is a error.....",e)

# def fun():
#     try:
#         return 10
#     finally:
#         return 20
# f1=fun()
# print(f1) 

# f=open('texts.txt','r')
# # f1=f.read()
# f1=f.readlines()
# print(f1)
# f.close()


# file1=open("texts.txt" ,"r")
# lines=file1.read()
# print(lines)

# file=open("texts.txt","w")
# lines=file.write("i am in bangaalore\n")
# lines=file.write("i am in mangaalore\n")
# lines=file.write("i am in udupi\n")
# print(lines)
# file.close()

# with open("texts.txt","r+") as f:
#     lines=f.read()
#     print(lines)

#     f.write("This ia a good ")
    
# file=open("texts.txt","w")
# file.write("This ia a good \n")
# file.write("awsome world is this ")
# file.cole()

# READING A LINE 
# i=0
# with open("texts.txt","r") as f:
#     i=i+1
#     while(True):
#         line=f.readline()
#         if not line:
#             break
#         m1=line.split(",")[0]
#         m2=line.split(",")[1]
#         m3=line.split(",")[2]
#         print(m1,m2,m3)
#         print(f"the mark of student {i} in math is: {m1}")
#         print(f"the mark of student {i} in math is: {m2}")
#         print(f"the mark of student {i} in math is: {m3}")
    # print(line)


# with open("texts.txt","w+") as f:
#     f.write(str(512)+'\n') 
#     f.write(str(12))
#     f.seek(0)
#     a=int(f.readline())
#     b=float(f.readline())
#     print(a+b)


# serialization 
# import json

# # Example data
# my_data = {
#     "name": "Alice",
#     "age": 30,
#     "city": "New York"
# }
# with open("my_data.json","w") as file:
#     json.dump(my_data,file)
#     # print()
# # DESERIALIZATION
# with open("my_data.json","r") as file:
#     de_data=json.load(file)
#     print(de_data)

import json
list1=[10,[20,30,40],[50,60,70],80,90]
with open("my_list.json","w") as file:
    json.dump(list1,file)
    file.seek(0)
    data=json.load(file)
    print(data) 
    file.close()   