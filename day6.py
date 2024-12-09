# class Date():
#     def __init__(self, year, month, day):
#         self.year=year
#         self.month=month
#         self.day=day

#     def __eq__(self,other):
#         if self.year==other.year and self.month==other.month and self.day==other.day:
#             return"Both dates are same"
#         else:
#             return "Both dates are not same"    

# d1=Date(2024,5,19)
# d2=Date(2024,5,19)
# print(d1==d2) 


# class Weather():
#     def __init__(self):
#         self.p=["dhim","rel","ball","pipe"]

#     def __in__(self,p):
#         return True if i in self.p else False   

# w=Weather("rel")
# if "rel" in w:
#     print("valid")
# else:
#     print("not valid")   


# a=(10,20)-(30,40)
# print(a)


# OPERATOR MUL OVERLOADING
# class Mul():
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b

#     def __mul__(self,other):
#         return self.a*other.a , self.b*other.b

# m1=Mul(10,11.6)
# m2=Mul(20,21.5)
# print(m1*m2)


# CALLING THE NAME OF THE CLASS
# class Demo():
#     def __init__(self):
#         print( "The name of the class is: ",self.__class__.__name__)

# d1=Demo()


#  METHODS
# INSTANCE
# CLASS
# STATIC
# class demo():
#     school="Milagres"
#     def __init__(self,a,b,c):
#         self.a=a
#         self.b=b
#         self.c=c
#     def disp(self):
#         return (self.a+self.b+self.c)/3

#     @classmethod   
#     def class_info(cls):
#         return cls.school   

#     @staticmethod
#     def Static_method():
#         return "This is a static method"

# d1=demo(10,55,88)
# print(d1.disp()) 
# print(demo.class_info())  
# print(demo.Static_method())     


# INNER CLASS




# class student():
#     def __init__(self,name,roll_num):
#         self.name=name
#         self.roll_num=roll_num
#         self.lap=self.Laptop(2024,16,512)

#     def disp(self):
#         print(self.name,self.roll_num) 
#         self.lap.disp()

#     class Laptop():
#         def __init__(self,year,ram,rom):
#             self.year=year
#             self.ram=ram
#             self.rom=rom

#         def disp(self):
#             print(self.year,self.ram,self.rom)

# s1=student("dhim",1)
# s1.disp()


# class car():
#     def __init__(self,brand,year,mileage):
#         self.brand=brand
#         self.year=year
#         self.mileage=mileage

#     def disp(self):
#         return f"the car is {self.brand} year of manufacturing is {self.year} and gives the mileage of {self.mileage}"

# class Bmw(car):
#     pass

# class audi(car):
#     def audi_disp(self):
#         return"This is audi"

# c1=Bmw("Mercedes",2024,24.1)
# print(c1.disp()) 
# c2=audi("BMW",2024,25)
# print(c2.disp()) 
# print(c2.audi_disp()) 
class A():
    def __init__(self):
        print("constructor of A ")
    def feature1(self):
        print("feature 1 is printed")


class B():
    def __init__(self):
        super().__init__()
        # super().feature1()
        print("costructor of B")
    def feature2(self):
        print("feature 2 is printed")
    def feature3(self):
        print("feature 3 is printed")

class C(A,B):
    def __init__(self):
        super().__init__()
        print("constructor of c is created")
    # def feature1(self):
    #     print("feature 1 is printed")


# obj1=A()        
# obj1.feature1()

obj3=C()
obj3.feature2()
# obj2.feature1()
# obj2.feature2()
# obj2.feature3()  #AttributeError: 'B' object has no attribute 'feature
