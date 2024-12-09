# def fun():
#     a=100
#     b=200
#     print(a,b,c)
# a=10
# b=12
# c="hello"
# fun()
# print(a,b,c) 
# def fun():
#     a=12
#     global b
#     b=10
#     print(locals())
#     print(globals()) 
# a=100
# global b
# b=30
# print(locals())
# print(globals())  
# fun()    
# def disp():
#     print("hello jii...")
#     def show():
#         print("qwertyu")
#     show()
# disp() 
# def fun1():
#     y=20
#     print(x,y)       
#     print(str(x))
#     def fun2():
#         z=30
#         print(x,y,z)
#         print(len(str(x)))
#     fun2()    
# x=10
# # print(len(str(x)))
# # fun1()
# def fun1():
#     a=10
#     print(a)
#     def fun2():
#         a=20
#         print(a)
#     fun2()
# fun1()  

# def test():
#     print(a)


# a=100 
# test()
# a=10
# b=20
# c=30
# # globals()["a"]
# # globals()["b"] 
# # globals()["c"]   
# print(a,b,c) 


# class Employee:
#     def set_data(self,name,age,address):
#         self.name=name
#         self.age=age
#         self.address=address
#     def disp_data(self):
#         print(self.name,self.age,self.address)    


# e1=Employee()
# e1.set_data("dhim",23,"blore") 
# e1.disp_data() 

# a="dhim"
# b=123
# # print(vars())
# print(dir()) 
# class fruits:
#     def __init__(self,name,color,quantity):
#         self.name=name
#         self.color=color
#         self.quantity=quantity

#     def disp(self):
#         print(self.name,self.color,self.quantity)

# f1=fruits("apple","red",15)
# f1.disp()
# print(vars(fruits))
# print(dir(fruits))
# print(vars(f1))
# print(dir(f1))
# class number:
#     def set_num(self,x):
#         self.num=x
#     def get_num(self):
#         print(self.num)
#     def isnegative(self):
#         if self.num<0:
#             print("negative")
#         else:
#             print("positive")
#     def isdivisible(self,x):
#         if x==0:
#             return False
#         if self.num%x==0:
#             return "divisible"
#         else:
#             return" not divisile"

# # n1=number()           
# # n1.set_num(3456)
# # n1.get_num()
# # n1.isnegative()
# # n1.isdivisible()


# import random
# def comp():
#     min_vla=1
#     max_val=6
#     z=random.randint(min_vla,max_val)
#     print(z)

# # comp()    
# while True:
#     player=int(input("Enter the no of players between(2,6): "))
#     # print(player)
#     # if player.isdigit():
#         # print("kbc")
#     if player<=2 or player>6:
#         print("enter valid player")
#     else:
#         print("valid")
#         break
# max_score=20
# player_score=[0 for _ in range(player)]
# print(player_score)
# while max(player_score)<max_score:
#     current_score=0
#     die_roll=input("do u want continue(s): ")
#     if die_roll.lower()!="s":
#         print("ended")
#         break
    
#     x=comp()
#     if x==1:
#         print("u r turn is done") 
#         break   
#     else:
#         current_score+=x
#         print("current score is: ",)
#     # print(player_score)


# def area(x):
#     return 3.14*x*x

# user=int(input("enter the radius: "))
# res=area(user)
# print(res)
# def even(lst):
#     sum=0
#     for i in lst:
#         if i%2==0:
#             sum+=i
#     return sum       
# lst=[]
# while True:
#     user=int(input("enter the number: "))
#     lst.append(user)
#     user2=int(input("do u want to continue(1): "))
#     if user2!=1:
#         break
# # print(lst)
# res=even(lst)
# print(res)
# class data:

#     def __init__(self,name,age,add):
#         self.name=name
#         self.age=age
#         self.add=add
#     def retrive(self):
#         return(self.name,self.age,self.add)

# d1=data("dhim",23,"blore")
# print(d1.retrive())
# class fruits:
#     count=0
#     def __init__(self,size,color):
#         self.size=size
#         self.color=color
#         fruits.count+=1
# f1=fruits(12,"red")
# f2=fruits(10,"blue")
# f3=fruits(13,"yellow")
# print(fruits.count)

class obj:
    def __init__(self,r,i):
        self.r=r
        self.i=i
    def __eq__(self,other):
        if self.r==other.r and self.i==other.i:
            return True
        else:
            return False

o1=obj(10,12)
o2=obj(10,12)
if o1==o2:
    print("o1 and o2 are equal")
else:
    print("not equal")
        

