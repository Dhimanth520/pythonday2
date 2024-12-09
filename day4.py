#variable length function
# def add(*b):
#     c=0 
#     for i in b:
#         c+=i
#     print(c)
# add(5,10,20,30)
# 
# keyworeded var len function
def person(name,**data):
    print(name)
    for key,value in data.items():
        print(f"{key} : {value}")


person("Dhim",age=23,add="bang",gender="male")
# 

# a=9
# def thing():
#     a=10
#     x=globals()["a"] 
#     print(id(x))
#     print("in fun",a)
#     globals()["a"]=15
#     print("out fun",a)
# thing()

# import day3
# print("hello boys : .......") 
# def sum():
#     print("result 1 is...")
# def sub():
#     print("result 2 is....")
# def main():
#     sum()
#     sub()
# if __name__=='__main__':
#     main()              

# def odd_even(str1):
#     even=0
#     odd=0
#     for i in str1:
#         if i%2==0:
#             even+=1
#         else:
#             odd+=1
            
#     return even,odd
# s=[1,2,3,4,5,6]
# even,odd=odd_even(s)   
# print("the number is odd: ",even)
# print("the number is even: ",odd)


# length of the name 
# def name():
#     user=input("Enter the name: ")
#     while(len(user)>5):
#         print("name is valid" ,user)
#         break
#     else:
#         print("name is not valid")
#     return user    
# name=name()

# fibonacci series


# def fib(n):
#     a=0
#     b=1
#     print(a)
#     print(b)
#     for i in range(2,n):
#         c=a+b
#         a=b
#         b=c
#         print(c)
# fib(5)        


# factorial of a number
# def factorial(n):
#     f=1
#     for i in range(1,num+1):
#         f*=i
#     print(f)
# num=4
# factorial(num)
# 
#  
# factorial using resurrsion 

# def fact_rec(n):
#     if n == 0:
#         return 1
#     else:
#         return n*fact_rec(n-1)


# res=fact_rec(5)
# print(res)        

# square using lambda 
# square=lambda a:a*a
# res=square(5)
# print(res)
 
 
# addition
# add=lambda a,b:a+b
# res=add(5,5)
# print(res) 

# filter
# numbers=[1,5,3,4,8,9,7,5,1,2]
# def even(i):
#     return i%2==0

# even_num=filter(even,numbers)
# print(list(even_num))   


# using lambda with filter
# numbers=[1,5,3,4,8,9,7,5,1,2]

# # def add_even(a,b):
# #     return a+b
# length=filter(lambda a:a%2==0,numbers)
# # mapping=list(map(lambda a:a*2,length))
# print(list(length))
# print(mapping)
# from functools import reduce
# # addition=reduce(add_even,mapping)
# addition=reduce(lambda a,b:a+b,mapping)
# print(addition)
