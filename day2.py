# string = "Python"
# for var in string:
#     print(var)
# string="Dhimanth"
# i=0
# while(i<len(string)):
#     print(string[i])
#     i+=1
# char=input("Enter the character: ")
# asciivalue=ord(char)
# print(asciivalue)
# char=input("enter the String: ")
# cpas=char.swapcase()
# print(cpas)
# char=input("Enter the letter: ")
# if char.islower():
#     print(" cap letters are:",char.upper())
# elif char.isupper():
#     print("the lowwer string is: ",char.lower())  
# else:
#     print("Enter a valid string") 
# s="bois love to drive"
# print(s)
# b=s.rfind(" ")
# print(b)
# s=input("enter the name: ")
# print("hi {}".format(s))
# s="hello world"
# print(s)
# lists=list(s)
# print(lists)
# lists[0]="H"
# newstr="".join(lists)
# print(newstr)
# print(type(newstr))
# s="hello world"
# a=s.replace("h","H")
# print(a)
# s="hello world"
# count=0
# for i in s:
#     count+=1
# print(count)
# s="good morning"
# dict={}
# for i in s:
#     keys=dict.keys()
#     if i in dict:
#         dict[i]+=1
#     else:
#         dict[i]=1 
# ss="w3schoolsw3"
# if len(ss)<2:
#     print("empty string")

# a=ss[:2]+ss[-2: ]    
# print(a)
# s="restart"
# first=s.find("r")
# second=s.find("r",first+1)
# finals=s[:second]+"$"+s[second+1:]
# print(finals)




# f string

# age =25
# name="dhimanth"
# sname="shetty"
# print(" he there my name is {} {} anmd my age is {}".format(name,sname,age))

# []
# letter=str(input("enter the string:"))

# char=str(input("Enter the character; "))
# first=letter.find(char)
# second=letter.find(char,first+1)
# final=letter[:second]+"$"+letter[second+1]
# print(final)



# a=[]
# i=0
# while (True):
#     data=input("Enter the data: ")
#     a.insert(i,data)
#     i+=1
#     print("do u want to continue: ")
#     print("yes:1")
#     print("no:2")
#     choice=int(input("enter the choice: "))
#     if choice==1:
#         continue
#     else:
#         break
# print(a)


# symetrical(length is is same) and palindrome

# String1=input("enter the string: ")
# mid= int(len(String1)/2)

# if len(String1)%2==0:
#     first=String1[:mid]
#     second=String1[mid:]
# else:
#     first=String1[:mid]
#     second=String1[mid+1:]

# if first == second[::-1]:
#     print("Symetrical")
# else:
#     print("Not")    

# palindrome
# str1=input("enter the string: ")
# str2=(str1.replace(" ","")).lower()

# if str1==str2[::-1]:
#     print("palindrome")
# else:
#     print("not")    


# a=[10,20,30,4,50,60,70,80]
# print(a[2])
# print(a[:5])
# print(a[6:])



# a=[]
# i=0
# needed=int(input("How many passwords are needed: "))
# max_size=needed
# # while(true)
# while(len(a) <= needed):
#     password=input("Enter the password: ")
#     if "@" in password:
#         a.insert(i,password)
#         i+=1
#     else:
#         print("Invalid")

#     choice=int(input("Enter the 1 to contniue and 2 for break: "))
#     if choice==1:
#         continue
#     else:
#         break


# print(a)
# a=[]
# i=0
# list1=input("Enter the Email: " )
# while(True):
#     if "@" in list1:
#         a.insert(i,list1)
#         i+=1
#     else:
#         print("Invalid")
#     choice=int(input("Enter the 1 to contniue and 2 for break: "))
#     if choice==1:
#        continue
#     else:
#         break
        
# print(a)
# a=[5,2,7,8,9,6,3,4,10,5,]
# print(sorted(a))
# print(sorted(a,reverse=True))

# multiplication table
# num=1
# while(num<=2):
    
#     multiplier=1
#     while(multiplier<=10):
#         print(f"{num} x {multiplier} = {num*multiplier}")
#         multiplier+=1
#     num+=1                
# for i in range(6):
#     print(i)
# else:
#     print("Loop finished!")
# my_dict={"name":"dhimanth","age":22,"gender":"male"}
# for key,value in my_dict.items():
#     print(f"key {key} : value : {value}")

# using enumerate function
# names=["dhimanth","abhin","yash"]
# for index,name in enumerate(names):
#     print(f"Index:{index} name:{name}")

# using zip function
# names=["dhimanth","abhin","yash"]
# marks=[100,99,98]
# for name,mark in zip(names,marks):
#     print(f"{name} scored {mark} marks")

# nums = [1, 2, 3, 4]
# for num in nums:
#     if num % 2 == 0:
#         nums.remove(num)
# print(nums)  # Output might not be as expected

# a=[10,20,30,40]
# b=[]
# for i in a:
#     c=i+1
#     b.append(c)
# print(b)

# a=[1,2,3,4]
# b=[i**i for i in a]
# print(b)  # Output: [11, 21, 31, 41]

# a=["hello","dhim","boy"]
# b=[]
# for i in a:
#     c=i.upper()
#     b.append(c)
# print(b)    