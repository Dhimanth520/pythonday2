# # PROTECTED ACCESS MODIFIER

# # class Student:
# #     # _name=None
# #     # _age=None
# #     # _marks=None
# #     def __init__(self,name,age,marks):
# #         self._name=name
# #         self._age=age
# #         self._marks=marks

# #     def _disp(self):
# #         print("Name of the sutdent us:",{self._name})
# #         print("marks of the sutdent us:",{self._marks})
# # class bag(Student):
# #     def __init__(self,name,age,marks):
# #         Student.__init__(self,name,age,marks)

# #     def display(self):
# #         print("name is: ",self._age)
# #         # accessing protected attribute from subclass 
# #         self._disp()
# #         # accessing protected method from subclass
# # b1=bag("dhim",23,100)
# # b1.display()

# # PRIVATE ACCESSS MODIFIER

# # class car:
# #     def __init__(self,door,window,tyres):
# #         self.__door=door
# #         self.__window=window
# #         self.__tyres=tyres

# #     def __display_info(self):
# #         print(self.__door)
# #         print(self.__window)
# #         print(self.__tyres) 

# #     def displayfunction(self):
# #         self.__display_info()

# # c1=car(4,4,5)
# # # c1.__display_info()   
# # c1.displayfunction()


# class students:
#     def __init__(self,name,age,marks):
#         self.name=name
#         self.age=age
#         self.marks=marks

#     def get_marks(self):
#         print( self.marks)
# class course:
#     def __init__(self,name,max_students):
#         self.name=name
#         self.max_students=max_students
#         self.students=[]

#     def add_students(self,student):
#         if len(self.students)<self.max_students:
#             self.students.append(student)
#             return True
#         return False
#     def avg_grade(self):
#         mark=0
#         for student in self.students:
#             mark += student.get_marks()
#         return mark/len(self.students)    

# s1=students("dhim",23,98) 
# s2=students("tim",23,67)
# s3=students("qwe",23,90)     
# s1.get_marks()
# c1=course("math",3)
# c1.add_students(s1)
# c1.add_students(s2)
# c1.add_students(s3)
# # print(c1.students[1].name)
# print(c1.avg_grade())


# import random
# print(random.randint(1111,1125))
# user=int(input("Enter the 4 digit  guess:"))
# print(user)
class bird:
    def fly(self):
        print("bird can fly.")

    def eat(self):
        print("bird can eat")
class dog:
    def run(self):
        print("can run fast")
    def eat(self):
        print("dag can eat") 
class person:
    def catch(self,dog):
        # dog.run(self)
        dog.eat(self)

b=bird()
d=dog()
p=person()
# p.catch(dog)
p.catch(bird)


