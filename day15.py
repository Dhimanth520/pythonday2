# class car:
#     def __init__(self,name,model,bhp):
#         self.name=name
#         self.model=model
#         self.bhp=bhp
#     def disp(self):
#         return self.name,self.model,self.bhp
#     def update(self,bhp,model):
#         self.bhp=bhp
#         self.model=model
# car_obj=car("mercedes","s-Class",600)   
# # car_obj()  
# print(car_obj.disp()) 
# car_obj.update("G-wagon",1200)          
# print(car_obj.disp()) 

# using str object
# class car:
#     def __init__(self,name,model,bhp):
#         self.name=name
#         self.model=model
#         self.bhp=bhp
#     def __str__(self):
#         return f"the car is{self.name}, model is {self.model} and bhp is {self.bhp}"
#     # def disp(self):
#     #     return self.name,self.model,self.bhp
#     def update(self,bhp,model):
#         self.bhp=bhp
#         self.model=model
# car_obj=car("mercedes","s-Class",600)   
# # car_obj()  
# print(car_obj) 
# car_obj.update("G-wagon",1200)          
# print(car_obj.disp())


# class example:
#     def __init__(self):
#         self.__private="its private"
#     def __private_method(self):
#         return"its a private one"

# obj=example()
# print(obj._example__private) 
# print(boj.__private_method())   
# print(obj._example__private)

# def printit():
#     print("hello..")
# class Message:
#     def disp(self,n):
#         printit()
#         return n
#     def show(self):
#         printit()
#         return "hello2"  

# printit()
# m=Message()
# print(m.disp("Dhimanth"))
# print(m.show()) 

# class add:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def __add__(self,other):
#         return self.a+other.a,self.b+other.b

#     def __sub__(self,other):
#         return self.a-other.a,self.b-other.b    
# a1=add(1,2)
# a2=add(3,4)
# # a3=a1+a2
# a3=a2-a1
# print(a3)
# a1.__add__(1,2)
# a2.__add__(3,4)
# class String:
#     def __init__(self,n):
#         self.n=n
#     def disp(self):
#         return self.n
#     def int(self):
#         return int(self.n)

# s1=String(123)
# print(s1.disp())  
# print(type(s1))          
# print(s1.int())
# print(type(k))
class department:
    def set_dept(self):
        self.__id=input("enter the dept id: ")
        self.__name=input("enter the fdept name: ")
    def disp(self):
        print("department id is:",self.__id) 
        print("the name is: ",self.__name)  
class Employee:
    def set_emp(self):
        self.__eid=input("enter the emp id: ")
        self.__ename=input("enter the emp name: ")
        self.obj=department()
        self.obj.set_dept()
        self.obj.disp()

    def disp(self):
        print("employee id: ",self.__eid)
        print("employee name is: ",self.__ename)
e1=Employee()
e1.set_emp()
e1.disp()            

