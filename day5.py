# import sys
# for p in sys.path:
#     print(p)

# GLOBALS
# a=1
# b=2
# c=3
# globals()['a']=10
# globals()["b"]=20
# globals()["c"]=30
# print(a,b,c)

# LOCALS
# def loc():
#     a=1
#     b=2
#     c=3
#     locals()['a']=10
#     locals()["b"]=20
#     locals()["c"]=30
#     print(a,b,c)
# loc()  


# a=10
# b=20
# print(globals())
# print(locals())  # locals() function returns the dictionary containing the current local symbol table. It


# CLASSES AND OBJECTS
# class my_class:
#     def config(self):
#         return "config"

# obj1=my_class()
# # print(obj1.config())  # TypeError: config() missing 1 required positional argument: '
# print(my_class.config(obj1))

# class student:
#     def set_data(self,name,age):
#         self.name=name
#         self.age=age
#     def disp_data(self):
#         print(self.name,self.age)

# s1=student()
# s1.set_data("Dhimanth",23)
# s1.disp_data()  

# s2=student()
# s2.set_data("yash",23) 
# s2.disp_data()        

# e3=student()
# e3.set_data("abhin",25)
# e3.disp_data()

# using __init__ method or constructor

# class Phone:
#     def __init__(self,brand,year,amt):
#         self.brand=brand
#         self.year=year
#         self.amt=amt
#     def get_data(self):
#         print("the details are: ",self.brand,self.year,self.amt)    

# p1=Phone("Samsung",2024,25000)
# p1.get_data()  


# class computer:
#     def __init__(self):
#         self.name="Samsung"
#         self.year=2024

#     def update(self):
#         self.name="dhimanth"

#     def compare(self,other):
#         if self.name==other.name:
#             return "same name"
#         else:
#             return "not same"

# c1=computer()
# c2=computer()
# c2.update()
# comp=c1.compare(c2)
# print(comp)
# print(c1.name)
# print(c1.year)
# print(c2.name)



# PROG1
# class Number:
#     def set_number(self,num):
#         self.num=num

#     def get_number(self):
#         return self.num

#     def print_number(self):
#         print(self.num)

#     def isnegative(self):
#         if self.num<0:
#             print("The number is negative")
#         else:
#             print("Not negative")

#     def isdivisible(self):
#         if self.num%2==0:
#             print("The number is divisible by 2")
#         else:
#             print("Not divisible")

#     def absolute_value(self):
#         if self.num>0:
#             print("the number is not absolute value",abs(self.num))
#         else:
#             print("the number is absolute value",abs(self.num))

# n1=Number()
# n1.set_number(18)
# n1.print_number()
# n1.isnegative()
# n1.isdivisible()
# n1.absolute_value()

# COUNT NUMBER OF OBJECTS 
# class Furit:
#     count=0
#     def __init__(self, name, quantity, color):
#         self.name = name
#         self.quantity=quantity
#         self.color=color
#         Furit.count+=1
#     def disp(self):
#         print(self.name,self.quantity,self.color)
        

# f1=Furit("Mango",10,"yellow")
# f2=Furit("apple",4,"red")
# f3=Furit("bananna",5,"light yellow")
# f1.disp()
# f2.disp()
# f3.disp()
# # f1.disp(count.disp)
# print(Furit.count)


# OPERATOR OVERLOADING
# class Operator():
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b

#     def __add__(self,other):
#         return self.a+other.a,self.b+other.b

#     def __sub__(self,other):
#         return self.a-other.a,self.b-other.b

# op1=Operator(1,2)
# op2=Operator(3,4)
# res1=op1+op2
# res2=op1-op2
# print(res1)
# print(res2)


# TYPE CONVERSION
class String():
    def __init__(self, s):
        self.s = s

    def disp(self):
        print(type(self.s))

    def __int__(self):
        return int(self.s)



obj=String("123")
obj.disp()
i=int(obj)
print(type(i))
