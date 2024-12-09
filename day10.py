# key_value={"dhim123":"dhim","yash123":"yash"}
# user_value=input("enter the user name: ")
# user_keypass=input("enter the passwword: ")
# for keys in key_value:
#     if keys==user_keypass:
#         print("password matched....")
#         break
#     else:
#         print("password notmatched")
#         while(keys!=user_keypass):
#             user_value=input("enter the user name: ")
#             user_keypass=input("enter the passwword: ")
#     print(keys)

# if():
#     print("asscess denied.....")
#     user_name=input("enter the user name: ")
#     password=input("enter the password: ")
# else:
#     print("access granted....")  

# for char in "lepord":
#     print(char)  # prints each character on a new line
# i=1
# while 1:
#     print(i,end=" ")
#     i+=1
#     if i>10:
#         break
# user=int(input("Enter the number: "))
# i=1
# while user>0:
#     i+=1
# print(i)
# n= int(input("enter the number: "))
# # while n>0:
# #     sum=0
# #     i=1
# #     sum=i+1
# # print(sum)
# sum=0
# for i in range(1,n+1):
#     sum+=i
# print(sum)

# number=int(input("Enter the number: "))
# for i in range(1,11):
#     print(f"{number} x {i} = {number*i}")


# start=25
# end=50
# for x in range(25,50):
# count=1
# # for x in range(11):
# #     print(f"loop {count} is running")
# #     count+=1
# while count<=10:
#     print(f"loop {count} is running")
#     count+=1
# i=15
# not while i<10:
# print(i)
# i-=1
# l,b,r=input("enter the length,breath,rdius: ").split()
# length=int(l)
# breath=int(b)
# radius=int(r)
# print("circumferance: ",2*(3.14*radius))
# print("perimeter: ",2*(length*breath))
# s="Rendezvous"
# for i in s:
#     print(i,end=" ")

# min,max=25,75
# print(f"{"Max value:"}{max:>5}")
# print(f"{"min value:":<15}{min:>10}")
# name="sanjay"
# number=7259792622
# print(f"{name:15}:{number:10}")
# lst=[12,72,15,36,48,7]
# lst.reverse()
# print(lst)


# a=[10,20,30,40]
# temp=a[0]
# a[0]=a[1]
# a[1]=temp
# print(a)

# main_list=[5,2,8,7,9,9,7,48,52,7]
# # main_list.sort()
# # print(list(set(main_list)))
# index_list=[1,4,6]
# operation=[main_list[i] for i in index_list ]
# print(operation)

# a=[2,4,5,6,7,8,9,8,75,85]
# print(a[0],a[-1])
# a[2]=10
# a.insert(4,20)
# a.remove(4)
# print(a[4:])
# print(a[::-1])
# list1=[]
# lit=[x for i in range(1,11) list1.append(i*i)]
# print(list1)
# import random
# a=[]
# i=1
# while i<=20:,
#     num=rando,m.randint(10,100)
#     a.append(num)
#     i+=1
# print( a)    
# for num in a:
#     if num>20 and num<50:
#         a.remove(num)
# print(a)
# lst=[10,20,30,40,50,60,70]
# lst.sort(reverse=True)
# print(lst)
# s="hello"
# x=list(s)
# print(x)
# lst1=[1,2,4,-9,7,-8,-6,5]
# pos=[]
# neg=[]
# for num in lst1:
#     if num>=0:
#         pos.append(num)
       
#     else:
#         neg.append(num)
# print(pos)
# print(neg)  
# list1=["dhim","yash","abhin"]
# for char in list1:
#     print(char[0])

# tp1=(8,5,2,4,6,9,7,4,53,2)
# for i,n in enumerate(tp1):
#     print(i,n)
# tp1=(1,2,3,4,5,6)
# # tp2=(7,8,9,10,11,12)
# # tp3=tp1+tp2
# # print(tp3)
# print(tp1.index(5))
# list1=[("Dhimanth",1,22),("abhi",2,22),("yash",3,22)]
# x=[]
# # i=0
# for ele in list1:
#     x.append(ele[0])
#     # i+=1
# print(x)
# tp2=(7,8,9,10,11,12)
# s=" ".join(tp2)/// not possible
# print(s)
# s1={1,2,3,4}
# s2={'a','b','c'}
# x=s1|s2
# print(x)
# s1={1,2,3,4}
# s2={'a','b','c',4}
# # s1.update(s2)
# x=s2&s2
# print(x)
