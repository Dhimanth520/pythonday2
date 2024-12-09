# # class parent():
# #     def __init__(self,name,id):
# #         self.name=name
# #         self.id=id
# #     def disp(self):
# #         print(self.name,self.id)   
# # class child(parent):
# #     def printit(self):
# #         print("child is printed")


# # p1=parent("dhim",12)  
# # p1.disp() 
# # c1=child("mayank",13)
# # c1.disp()
# # c1.printit()
# # p1.printit()

# class person():
#     def __init__(self,name,uid,age):
#         self.name=name
#         self.uid=uid 
#         self.age=age
#     def get_name(self):
#         return self.name 
# class Employee(person):
#     def __init__(self,name,uid,age,address):
#         super().__init__(name,uid,age)
#         self.address=address
#     # def isemployee(self):
#     #     return True
# # p1=person("dhim",12,23)   
# # print(p1.get_name())
# e1=Employee("yash",14,23,"blore")
# print(e1.get_name())
# class person():
#     def __init__(self, name, uid, age):
#         self.name = name
#         self.uid = uid
#         self.age = age

#     def get_name(self):
#         return self.name
# class Employee(person):
#     def __init__(self, name, uid, age, address):
#         super().__init__(name, uid, age)
#         self.address = address

# # Create an instance of Employee
# e1 = Employee("yash", 14, 23, "blore")
# print(e1.get_name())  # Output: yash
# from abc import abstractmethod
# class Shape():
#     @abstractmethod
#     def draw(self):
#         pass
# class Circle(Shape):
#     def draw(self):
#         print("hi")

# class Rectangle(Shape):
#     def draw(self):
#         print("hello")
# # s=Shape()
# # print(s.draw())
# c=Circle()
# c.draw()
# r=Rectangle()
# # r.draw()
# class base():
#     def __one(self):
#         print("in base.__one")
#     def func(self):
#         self.__one()
# class derived():
#     def __one(self):
#         print("in derived.__one")
#     def func(self):
#         self.__one()            
# b1=base()
# b1.func()
# d1=derived()
# d1.func()
# from abc import ABC,abstractmethod
# class Character(ABC):   
#     @abstractmethod
#     def patriotism(self):
#         pass
# class actor():
#     def style(self):
#         print("he is a actor")
# class person(Character,actor):
#     def patriotism(self):
#         print("this is a pratriotism")

#     def style(self):
#         print("actor in 2")

#     def do_acting(self):
#         print("this is a new method")
# p1=person()
# p1.patriotism()
# p1.style()
# p1.do_acting()        
# word=["a","dhim","yash","prad"]
# numbers=[1,2,3,4]
# # for ele in zip(word,numbers):
#     # print(ele[0],ele[1])
#     # print(*ele)
# it=zip(word,numbers)
# print(list(it))
# print(type(it))
# 0
# import sys
# lst=[i*i for i in range(10)]
# print(lst)
# print(sys.getsizeof(lst))
# import math
# z=math.pow(4,2)
# print(int(z))
# try:
#     a=int(input("enter the value: "))
#     b=int(input("enter the value: "))
#     c=a/b   
#     print(c)
# except Exception as e :
#     print(e)    
# try:
#     while True:
#         num=int(input("enter the number: "))
#         if num>0:
#             print("the number is positive: ",num*num)
#         else:
#             raise ValueError("negative number")
# except ValueError as e:
#     print(e)

# while True:
#     try:
#         user=int(input("enter the number: "))
#         break
#     except ValueError as e:
#         print(e)
#     print("you entered...",user )   
# msg1="hello there 1\n"
# msg2="hello there 2\n"
# msg3="hello there 3\n"
# msg4="hello there 4\n"
# with open('message','w') as f:
#     f.write(msg1)   
#     f.write(msg2)
#     f.write(msg3)
#     f.write(msg4)

# with open('message','r') as f:
#     data=f.read()
#     print(data)
import json
# lst=[10,20,30,40,50,60]
# with open ("message2","w+") as f:
#     json.dump(lst,f)
#     f.seek(0)
#     inlst=json.load(f)
#     print(inlst)

lst=(10,20,30,40,50,60)
with open ("message3","w+") as f:
    json.dump(lst,f)
    f.seek(0)
    inlst=json.load(f)
    print(tuple(inlst))



