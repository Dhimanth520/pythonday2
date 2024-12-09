# lst=[1,2,3,4,5,6,8]
# print(*lst)
# tupl=[1,2,3,4,5,6,8]
# print(*tupl)
# def trying():
#     print("hi")
#     trying()
# trying()

# recursive function
# demopass="1234"
# def upass():
#     user_pass=input("enter the password: ")
#     if user_pass.isdigit():
#         if user_pass==demopass:
#             print("access granted..")
#         else:
#             print("invalid..")
#             upass()
#     else: 
#         print("enter a vlid password")        
#         upass()
        
# # user_pass=input("enter the password: ")
# upass() 

# def fact(n):
#     if n==0:
#         return 1
#     else:
#         res=n*fact(n-1) 
#     return res 
# num=int(input("enter the number: "))          
# print(fact(num))
# print(result)

# head and tail resursion
# def head(n):
#     if n==0:
#         return
#     else:
#         print(n)//tail
#         head(n-1)//if statement is getting printted first then it called tail recursion else it is called head recursion 
#         # print(n)
# head(10)    
# ITERATIVE APPROACH        
# def walk(n):
#     for i in range(1,n+1):
#         print(i)
    
# walk(5)    

# RECURSIVE APPROACH 
# def walk(n):
#     if n==0:
#         return
#     # print(n)
#     walk(n-1)
#     print(n)
# walk(5)  

# def mul(num):
#     res=1
#     for i in range(2,num+1):
#         res=res*i
#     return res     
# print(mul(5))        

# def rfun(number):
#     if number!=0:
#         num=number%10
#         number=number//10
#         sum=num+rfun(number)
#     else:
#         return 0
#     return sum        
# number=int(input("enter the number: "))
# print(rfun(number))

# user=int(input("enter the number: "))
# sum=0
# while user>0:
#     num=user%10
#     sum=sum+num
#     user=user//10
# print(sum)
# def fun(x,y):
#     if x==0:
#         return y
#     else:
#         return fun(x-1,x*y)
# print(fun(4,2))  
# def func(n):
#     return lambda a:a*n
# myfun=func(10)
# print(myfun(2))
# lst=[1,2,3,4,5,6]
# print((lambda l:sum(l)/len(l))(lst))
# z=sum(lst)
# y=len(lst)
# print(z/y)

# map

# def sqr(n):
#     return n*n*n
# # print(sqr(2))
# n=[1,2,3,4,5]
# z=list(map(sqr,n))
# print(z)

# filter

# def filt(n):
#     return n>5
# lst=[2,4,6,8]
# newl=list(filter(filt,lst))
# print(newl)

# reduce

# from functools import reduce
# def red(a,b):
#     return a+b
# lst=[2,4,6,8]
# new=reduce(red,lst)
# print(new)    

# MAP WITH lambda
# lst=[1,2,3,4,5,6,7,8]
# x=list(map(lambda a:a*a, lst))
# print(x)

# filter with reduce
# lst=[1,2,3,4,5,6,7,8]
# x=list(filter(lambda a:a>4,lst))
# print(x)

# reduce with reduce
# from functools import reduce
# lst=[1,2,3,4,5,6,7,8]
# x=reduce(lambda a,b:a+b,lst)
# print(x)


# def fun():
#     print("fun")

# def disp():
#     print("disp")

# def msg():
#     print("msg")

# lst=[fun,disp,msg] 
# for i in lst:
#     i()       

# lst1=[1,2,3,4,5,6,7,8,9]
# lst2=[9,8,7,4,5,6,3,2,1]
# res=list(map(lambda a,b:a+b,lst1,lst2))
# print(res)
# lst=["malayalam","drawing",1234321]
# for i in lst:
#     n=str(i)
#     if n[:]==n[::-1]:
#         print("palindrome",n)
#     else:
#         print("not palindrome",n)
# x=list(map(lambda a: a[:]==a[::-1],lst)) 
# print(x)       
# result=lambda x:f"{x} is even" if x%2==0 else f"{x} is odd "
# print(result(10))
# print(result(13))


def disp():
    print("hello")

def show():
    print("hi")
if __name__=="__main__" :
    disp()
    show()
    print(__name__)
# disp()
# show()    