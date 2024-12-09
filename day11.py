# s={5,78,9,6,58,7}
# # s.remove(9)
# # s.remove(3)
# # s.discard(3)
# s1={5,7,8,9,6,3,2,1,4,5}
# print(s)
# accessing a tuple using indexing
# s=("dhim","yash","abhi","shameel","abhin")
# for x in range(len(s)):
#     print(x,s[x])
# s={"dhim","yash","abhi","shameel","abhin"}
# for x,i in enumerate(s):
#     print(x,i)
# s1={10,20,30,40,50,60}
# s2={10,20,30,40,50,60}
# print(*s1,*s2)
# s2={10,20,30,(11,22,30),40,50,60}
# print(s2)
# s1={50,40,60,20,10,30,40,80}
# s1.sorted()  //  sorted property not present
# print(s1)
# a={"abhin","blen","Akash","Belavita"}
# x=set()
# y=set()
# for name in a:
#     if name.startswith("a"):
#         x.add(name)
#     elif name.startswith("A"):
#         x.add(name) 
#     elif name.startswith("B"):
#         y.add(name)        
#     else:
#         y.add(name)
# print(x)
# print(y)       
# 
# 
#  
# eset=set()
# count=0
# # delset=set()
# name=input("Enter the names: ")
# eset.add(name)
# count+=1
# while(count<5):
#     name=input("Enter the name: ")
#     eset.add(name)
#     count+=1

# print(eset)
# add_name=input("enter the name to be added: ")
# eset.add(add_name)
# del_names=input("enter the name to be deleted: ")  
# eset.remove(del_names)
# print(eset)

# cources={"cs1":"cse","cs2":"ec","cs3":"it"}
# for k,v in reversed(cources.items()):
#     print(k,v)


# d={"cs1":"cse","cs2":"ec","cs3":"it"}
# for k,v in d.items():
#     print(k,v)

# myfamily = {
#   "child1" : {
#     "name" : "Emil",
#     "year" : 2004
#   },
#   "child2" : {
#     "name" : "Tobias",
#     "year" : 2007
#   },
#   "child3" : {
#     "name" : "Linus",
#     "year" : 2011
#   }
# }
# for item,obj in myfamily.items():
#     print(obj)


# key_value = {"dhim123": "dhim", "yash123": "yash"}

# user_value = input("Enter the username: ")
# user_keypass = input("Enter the password: ")

# found = False
# for key, value in key_value.items():
#     if key == user_keypass and value == user_value:
#         print("Password matched...")
#         found = True
#         break

# if not found:
#     print("Password not matched")

# x={"dhim","abhay","yash"}
# y=100
# print(type(x))
# print(type(y))
# print(dict.fromkeys(x,y))

# key_value={"dhim123":"dhim","yash123":"yash"}
# user_value=input("enter the user name: ")
# user_keypass=input("enter the passwword: ")
# for key ,value in key_value.items():
#     if key==user_keypass and value==user_value:
#         print("password matched....")
#         break
#     else:
#         print("password notmatched")
#         while(key!=user_keypass):
#             user_value=input("enter the user name: ")
#             user_keypass=input("enter the passwword: ")
    
    # print(key)
# from operator import itemgetter
# lst1=[10,20,30,40,50]
# get=itemgetter(4)
# element=get(lst1)
# print(element)
# import re
# txt="this a test environment st"
# x=re.findall("st",txt)
# print(x)
# txt="this will get executed all the time"
# x=re.sub("l",'  and',txt)
# print(x)

# key_value={"dhim123":"dhim","yash123":"yash"}
# user_value=input("enter the user name: ")
# user_keypass=input("enter the passwword: ")
# flag=0
# for key,value in key_value.items():
#     if key==user_keypass and value==user_value:
#         print("password matched....")
#         flag=1
#         break
# if flag!=1:
#     print("passwored not matched...").
# num=int(input("enter a number: "))
# i=2
# while i<num:
#     if num%i==0:
#         print(num,"is not a prime number")
#         break
#     i+=1
# else:
#     print("number is prime..")

# for x in range(0,25+1):
#     if x%2!=0:
#         print(x,end=" ")

a=int(input("Enter the side a: "))
b=int(input("Enter the side b: "))
c=int(input("Enter the side c: "))
if a*a + b*b == c*c:
    print("this is a triplet....")
else:
    print("this is not a triplet...")








