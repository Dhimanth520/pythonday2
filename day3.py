# num=[]
# for i in range(1500,2701):
#     if i %7==0 and i%5==0:
#         num.append(i)
# print(num)

# user=int(input("want to convert to celcius(1) or to farnheit(2): "))
# if user==1:
#     num=int(input("enter the temperature to be converted to fahrenheit: "))
#     far=num*9/5+32
#     print("F is equal to:",far)
# else:
#     num=int(input("enter the fahrenheit to be converted to celcius: "))
#     cel=(num-32)*5/9
#     print("C is equal to:",cel)


# import random
# random_int=random.randint(1,5)
# user_guess=int(input("Guess a number: "))
# while(True):
#     if user_guess==random_int:
#         print("Well guessed")
#         print("The random guess was: ",random_int)
#         break
#     else:
#         print("Wrong guess, try again")
#         print("The random guess was: ",random_int)
#         break

# word=input("Enter the word: ")
# word=word[::-1]
# print(word)

# number=(1,2,3,4,5,6,7,8,9)
# count_odd=0
# count_even=0
# for i in number:
#     if i%2==0:
#         count_even+=1
#     else:
#         count_odd+=1
# print(count_even)
# print(count_odd)      

# Write a Python program that iterates the integers from 1 to 50. For multiples of three print "Fizz" 
# instead of the number and for multiples of five print "Buzz". For numbers that are multiples of three 
# and five, print "FizzBuzz".
# for i in range(1,51):
#     if (i%3==0) and (i%5==0):
#         print("Multiple of 3 and 5 :Fiz Buzz",i)     
#     elif i%3==0:
#         print("Multiple of 3 :Fizz",i)
#     elif (i%5==0) :
#         print("Multiple of 5 :Buzz",i)     

# Functions
# def invoice(username,amount,date):
#     print(f"hello {username}")
#     print(f"your invoice is {amount} due on {date}")

# invoice("dhimanth",25000,"1/5/2004")

# with para nd no return type
# def add_num(x,y):
#     a=x
#     b=y
#     c=a+b
#     print(c)
# add_num(10,20)    

# fun with no para with retur type
# def add_num():
#     a=10
#     b=20
#     c=a+b
#     return c
# ref=add_num() 
# print(ref)   

# with parameter and with return type
# def add_num(x,y):
#     a=x
#     b=y
#     c=a+b
#     return c
# ref=add_num(10,20) 
# print(ref) 


# keyword argument
# def greet(name,msg):
#     return print(f"{msg}, {name}")
# greet(name="dhim",msg="hello")

#lambda function 
# res=lambda num:num*num
# print(res(10))
# res=lambda a,b:a+b
# print(res(10,20))  # Output: 30

# t1 =(10,20,50,4,50,60,)
# print(t1[3])
# def opp(x,y):
#     res1=x+y
#     res2=x-y 
#     res3=x*y 
#     return res1,res2,res3
# result=opp(10,20)
# print(result)  
# 

# prime number
# num=int(input("Enter the number in then range [2 to n]: "))
# for i in range (2,num):
#    if num % i==0:
#     print(f"{num} is not a prime number")
#     break
# else:
#     print(f"Prime {num}")

# print(4%6)
 
# s1={1,2,3,4,5,6,7,7}
# print(s1)
# a=set()
# for i in range(3):
#     ele=int(input("enter the number: "))
#     a.add(ele)
#     print(a)  # Output: {1, 2, 3}  # Output:

# emp={"name":"dhim","age":"22","add":"bang"}
# # print(emp.keys())
# # print(emp.values())
# # print(emp.items())

# for key ,value in emp.items():
#     print(key," ",value)
# d={1:100,2:300,4:500,5:600,6:700}
# print(d[1]) 
# # print(d.get(1))  # Output: 100
# # print(d.get(1,"not found"))  # Output: 100
# # print(d.get(7,"not found"))  # Output: not found
# # print(d.pop(1))  # Output: 100
# # print(d)  # Output: {2: 300, 4: 500,
# d1=d   #shallow copy
# print(d1)
# d2=d.copy()
# print(d2)  # Output: {1: 100, 2: 300,
# print(d[5])
# def max_num(x,y,z):
#     if x>y and x>z:
#         print("x is largest")
#     elif y>x and y>z:
#         print("y is largest")
#     else:
#         print("z is largest")        
#     return x,y,z    
# max_num(5,9,2)    

# def sum_list(list1):
#     sum = 0
#     for i in list1:
#         sum+=i
#     return sum
# s=[1,2,3,4,5]    
# print(sum_list(s))

# def mul_list(list1):
#     mul = 1
#     for i in list1:
#         mul*=i
#     return mul
# s=[1,2,3,4,5]    
# print(mul_list(s))

# def reverse_str(str1):
#     return str1[::-1]
# str1="hello"    
# print(reverse_str(str1))
# def thing():
#     print("hello world")
#     print("how r u ")
    
# if __name__=="__main__":
#     thing()
from day4 import sum
def fun1():
    sum()
    print("hello world")

def fun2():
    print("how r u ")

def main():
    fun1()
    fun2()
main()        