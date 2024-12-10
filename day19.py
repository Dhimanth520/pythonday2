# class student:
#     school_name="qwe school"
#     name="qweg"
#     def __init__(self,name,marks,age):
#         self.name=name
#         self.marks=marks
#         self.age=age

#     def disp(self):
#         return self.name,self.marks,self.age    
# s1=student("dhim",21,21)
# # print(s1.school_name)
# print(s1.disp()) 
# class student :
#     def __init__(self,name,mark1,mark2,mark3):
#         self.name=name
#         self.mark1=mark1
#         self.mark2=mark2
#         self.mark3=mark3 
#     def avg(self):
#         return (self.mark1+self.mark2+self.mark3)/3

# s1=student("dhim",50,97,98)
# print(s1.avg())
# class student :
#     def __init__(self,name,mark):
#         self.name=name
#         self.mark=mark
#     @staticmethod
#     def func():
#         print("hi wenfvnuevuf")    
#     def avg(self):
#         sum=0
#         for i in self.mark:
#             sum+=i
#         print(f"hi {self.name} ur avg mark is: ",(sum/3))

# s1=student("dhim",[90,50,100])
# s1.avg()   
# s1.func() 
# Abstraction
# class car:
#     def __init__(self):
#         self.acc=False 
#         self.brk=False
#         self.clutch=False
#     def start(self):
#         self.clutch=True
#         self.acc=True
#         return "The car has stratted...."
            
# c1=car()
# print(c1.start())                
# class Account:
#     def __init__(self,balance,acc_no):
#         self.balance=balance
#         self.acc_no=acc_no

#     def debit(self,amount ):
#         self.balance-=amount
#         print(f"The {amount} was debited from the account ")
#         print("the total balance is: ",self.total_balance())

#     def credit(self,add):
#         self.balance+=add
#         print(f"the {add} amount was added to the existing balance")
#         print("the uopdated balance is",self.total_balance())    
#     def total_balance(self):
#         return self.balance

# a1=Account(10000,1234)
# # print(a1.balance)
# # print(a1.acc_no) 
# a1.debit(500)
# a1.credit(1200) 
# a1.credit(25000)
# a1.debit(5500)  
#!/bin/python3





# n = int(input(3).strip())
# if n%2==0:
#     print("Weird")
# elif n%2==0:
#     for n in range(2,5):
#         print("Not Weird")
#         break
# elif n%2==0:
#     for n in range(6,10):
#         print("Weird")
#         break
# elif n%2==0 and n>20:
#     print("Not Weird") 
# n = int(input("enter the number: "))
# if n%2!=0:
#     print("Weird")
# elif 2<n<5:
#     print("Not Weird")
# elif 6<n<20:
#     print("Weird")
# elif n>20:
#     print("Not Weird")

# INHERITANCE

# class Animal:
#     name=""
#     def eat(self):
#         print("animal is eating..")
# class Dog(Animal):
#     def disp(self):
#         print("the name of the dog is ",self.name)        
# d1=Dog()
# d1.name="bruno"
# d1.eat()
# d1.disp()  

# MULTILEVEL INHERITANCE


# class mamal():
#     def super_info(self):
#         print("its a mamal super class")
# class winged_animal(mamal):
#     def derived_info1(self):
#         print("this is wnged animal derived class")
# class bat(winged_animal):
#     def derived_info2(self):
#         print("its a bat derived class2 ")
# b1=bat()
# b1.super_info()
# b1.derived_info1()
# b1.derived_info2()   

# MULTIPLE INHERITANCE
# class mamal():
#     def super_info(self):
#         print("its a mamal super class")
# class winged_animal():
#     def derived_info1(self):
#         print("this is wnged animal derived class")       
# class bat(winged_animal,mamal):
#     def derived_info2(self):
#         print("its a bat derived class2 ")        
# b1=bat()
# b1.derived_info1()
# b1.super_info()  

# getting the class name 

# class Beemer():
#     def name(self,name):
#         return name
# b1=Beemer()
# print(b1.__class__.__name__) 

# LEAP YEAR

# year=int(input("enter the year: "))
# def leap_lear(year):
#     if year%400==0 and year%100==0:
#         print(f"the year{year} is a leap year")
#     elif year%4==0 and year%100!=0 :
#         print(f"the year {year} is leap year")
#     else:
#         print(f"the year {year} not a leap year") 
# year=int(input("enter the year: ")) 
# leap_lear(year)       

# PRIME NO 

# num=int(input("enter the number: "))
# def prime(num):
#     flag=False
#     if num==0 or num==1:
#         print(f"number {num} is not a prime number")
#     elif num>1:
#         for i in range(2,num):
#             if num%i==0:
#                 flag=True
#                 break
#         if flag==True:
#             print(f"The number {num} is prime")
        
#         else:
#             print(f"the number {num} is not prime")    
# num=int(input("enter the number: "))
# prime(num)

# SUM OF NATURAL NUMBERS

# def nat_sum(num):
#     sum=0
#     for i in range(1,num+1):
#         sum+=i
#     print(sum)
# num=int(input("enter the number: ")) 
# nat_sum(num)  

# REVERSE A NUMBER
# num = 1234
# reversed_num = 0

# while num != 0:
#     digit = num % 10
#     reversed_num = reversed_num * 10 + digit
#     num //= 10

# print("Reversed Number: " + str(reversed_num))

# def rev_num(num):
#     reversed_num=0
#     while num!=0:
#         digit=num%10
#         reversed_num=reversed_num*10+digit
#         num//=10
#     print(reversed_num)
    
# num=int(input("enter the number: "))
# rev_num(num)   
def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def mul(num1,num2):
    return num1*num2        
def div(num1,num2):
    return num1/num2
num1=int(input("Enter the number:"))
num2=int(input("enter the number: "))
choice=int(input("enter the choice 1(add), 2(sub), 3(mul), 4(div): "))
if choice==1:
    add(num1,num2)
    break
elif choice==2:
    if num1>num2:
        sub(num1,num2)
    else:
        print("enter the numbers proberly")
        break
elif choice==3:
      mul(num1*num2)
elif choice==4:
          


