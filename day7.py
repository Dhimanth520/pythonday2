
# ABSTRCAT CLASSES

# import abc
# class parent():
#     def display():
#         pass

# class child(parent):
#     def display():
#         print("Hello, I am a child class")


# print(isinstance(child(),parent))
# print(issubclass(child,parent)) 

# from abc import ABC
# class parent(ABC):
#     def display(self):
#         print("base class: ")

# class child(parent):
#     def display(self):
#         super().display()
#         print("derived class")

# c1=child()
# c1.display()  # Output: base class: derived class

# from abc import ABC,abstractmethod
# class parent(ABC):
#     @abstractmethod
#     def display(self):
#         pass
# class child(parent):
#     def display(self):
#         print("Hello, I am a child class")
# class subchild(parent):
#     def display(self):
#         print("this is the second child class..")

# c1=child()
# c1.display()
# s1=subchild()
# s1.display()

# class Shape():
#     def disp():
#         print("general class: ")

# class Circle(Shape):
#     def disp(self):
#         print("This is a circle")
# class Rectangle(Shape):
#     def disp(self):
#         print("This is a rectangle")

# s1=Shape()
# c1=Circle()
# r1=Rectangle()
# print(isinstance(Shape,Rectangle)) 
# # print(isinstance(Shape,Cirlce()))    
# # print(isinstance(Circle,Shape))   
# print(isinstance(r1,Shape))
# print(isinstance(Rectangle,Circle))
# print(isinstance(c1,Shape)) 
# # print(isinstance(Rectangle,c1))

# SIMPLE INHERITANCE
# class base():
#     def disp(self):
#         print("base class")
#     def method(self):
#         print("This is a method...")

# class derived(base):
#     def method(self):
#         print("this is the method in derived class ")


# b=base()
# b.method()
# d=derived()
# d.method()      


# from abc import ABC,abstractmethod
# class Printer(ABC):
#     def print(self):
#         pass
# class Laserprinter(Printer):
#     def print(self):
#         print("this is a laserprinter..")
# class Inkjetprinter(Printer):
#     def print(self):
#         print("this is a inkjetprinter..")       
# lp=Laserprinter()
# lp.print()
# ij=Inkjetprinter()
# ij.print()
# p=Printer()
# p.print()


# from abc import ABC,abstractmethod
# class Printer(ABC):
#     @abstractmethod
#     def __init__(self,n):
#         self.name=n
#     def print(self,doc_name):
#         pass
# class Laserprinter(Printer):
#     def __init__(self,n):
#         super().__init__(n)
#     def print(self,doc_name):    
#         print("this is a laserprinter..")
#         print("the file name id ",doc_name)
# class inkjetprinter(Printer):
#     def __init__(self,n):
#         super().__init__(n)
#         def print(self,doc_name):
#             print("this is a inkjetprinter..")
#             print("the file name id ",doc_name)
# # p=Laserprinter("laserjet100") 
# # p.print("file1.txt")
# p=inkjetprinter("inkjet100")
# p.print("file2.txt")


# from abc import ABC,abstractmethod 
# class Character(ABC):
#     @abstractmethod
#     def patriotism(self):
#         pass
# class Actor():
#     def Style(self):
#         print("styling ")
# class Person(Actor,Character):
#     def patriotism(self):
#         print("he is a patriotic actor..")
#     def Style(self):
#         print("styling ")
#     def do_acting(self):
#         print("he is doing acting..")
# p=Person()
# p.Style()
# p.patriotism()
# p.do_acting()

# from abc import ABC,abstractmethod 
# class Character(ABC):
#     @abstractmethod
#     def patriotism(self):
#         pass
# c1=Character()

# ABSTRACT CLASS
# from abc import ABC,abstractmethod
# class animal:
#     @abstractmethod
#     def eat(self):
#         pass
# class bird(animal):
#     def eat(self):
#         print("Bird eats") 
# b=bird()
# b.eat()
# a=animal()
# a.eat()  # Raises a TypeError: Can't instantiate abstract class animal with abstract methods


# a=10.0
# b=20
# print(float.__add__(a,b))
# class add:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b

#     def __add__(self,other):
#         return self.a+other.a,self.b+other.b
# a1=add(10,20)
# a2=add(30,40)
# result =a1+a2
# print(result)

# lists=[(1,'a'),(2,'b'),(3,'c')]
# list1,list2=zip(*lists)
# print(list1)
# print(list2)  


# lst =[10,20,30,40]
# it=iter(lst)
# print(next(it))  
# print(next(it))   
# print(next(it))   
# print(next(it))  
# print(next(it)) 



# def numbers():
#     n=1
#     while(n<=10):
#         sq=n*n
#         yield sq
#         n+=1
# num=numbers()
# for i in num:
#     print(i)

# list1=[]
# count=0
# for i in range (0,10):
#     if i%2!=0:
#         count=+i
#         list1.append(count)
# # print(list1)
# list1[3]=[2,4,6,8,10]
# print(list1)
# flatlist=[elements for innerlist in list1 if isinstance(innerlist, list) for elements in innerlist ]
# print(flatlist)
# for inn erlist in list1:
#     for elements in innerlist:
#         print(elements)# Output: 2 4 6 8 10
# res=sorted(list1)
# print(res)

list1 = []
count = 0
for i in range(0, 10):
    if i % 2 != 0:
        count += i
        list1.append(count)

list1[3] = [2, 4, 6, 8, 10]

flatlist = []
for element in list1:
    if isinstance(element, list):
        flatlist.extend(element)  # Extend the flatlist with elements of the nested list
    else:
        flatlist.append(element)  # Append the single element to the flatlist
result=sorted(flatlist)
print(result)
# Initialization:

# flatlist = []: An empty list is created to store the flattened elements.
# Iterating Over the Nested List:

# for element in list1: This loop iterates over each element in the list1.
# Checking for Nested Lists:

# if isinstance(element, list): This condition checks if the current element is a list.
# Flattening Nested Lists:

# flatlist.extend(element): If the element is a list, the extend() method is used to add all elements of the nested list
#  to the flatlist. This effectively merges the nested list into the flatlist.
# Appending Single Elements:

# else: If the element is not a list (i.e., it's a single value), the append() method is used to add the element to the
#  flatlist.