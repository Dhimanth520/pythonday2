# def loud(txt):
#     return txt.upper()
# def quit(txt):
#     return txt.lower()
# def abc(func):
#     txt=func("heLlo")
#     print(txt)
# abc(loud) 
# abc(quit) 

# def divisor(x):
#     def divident(y):
#         return y/x
#     return divident 
# divide=divisor(2)
# print(divide(50))    
# x=lambda n:n*n
# print(x(10))
# print(res)    
# check=lambda age:"eligible" if age>=18 else "not eligible"
# print(check(10))
# students=[("dhim","A",60),
#         ("yash","r",90),
#         ("qwe","b",99), 
#         ("asd","o",77)]

# x=students        
# row=lambda rows:rows[2]
# students.sort(key=row)
# for i in students:
#     print(i)
# store=[("bmw",25),
#         ("benz",30),
#         ("skoda",12)]
# converaion=lambda data:(data[0],data[1]*84)
# z=list(map(converaion,store))
# for i in z:
#     print(i)    
# from functools import reduce    
# lst=[1,2,3,4,5]
# z=reduce(lambda x,y:x+y,lst)
# print(z)
# lst=[]
# for i in range(1,11):
#         lst.append(i*i)
# print(lst)
# squres=[i*i for i in range(1,11)]
# print(squres)
# lst=[70,50,20,25,90,100,50,60,68,89,40]
# marks=list(filter(lambda mark:mark>=50,lst))
# marks=[i if i>60 else "failed" for i in lst]
# marks=[i for i in lst if i>60 ]
# print(marks)        
# cities_faran={"banglore":40,"delhi":50,"sudhi":60}
# temp={key:round((value-32)*(5/7)) for (key,value) in cities_faran.items()}
# print(temp)
# cities_faran={"banglore":"cloudy","delhi":"cloudy","saudhi":"cloudy","uae":"sunny"}
# wether={key:value for key,value in cities_faran.items() if value=="cloudy"}
# print(wether)
# cities={"bangalore":16,"delhi":18,"udupi":25,"mangalore":28,"mumbai":19,"up":18}
# wether={key:("cold" if value<20 else "warm") for key,value in cities.items()}
# print(wether)
# user_name=["dhim","yash","abhay","abhin"]
# password=[1234,456,789,741]
# id=zip(user_name,password)
# for x in id:
#         print(x) 
# import time
# print(time.ctime())
# def balance_amt():
#     print(f"The the balance amount is {balance}")
# def add_amt():
#     amount=int(input("enter the amount: "))
#     if amount<0:
#         print("please enter a valid amount..")
#         return 0
#     else:
#         print(f"amount {amount} added successfully") 
#         return amount   
# def withdraw():
#     debit=int(input("enter the amount: "))
#     if debit>balance:
#         print("insuffcient balance")
#         return 0
#     elif debit<0:
#         print("enter a valid amount..") 
#         return 0   
#     else:
#         print(f"amount {debit} withdrawn successfully") 
#         return debit

# balance=0
# while True:
#     print("enter to c balance(1): ")
#     print("enter to c add money(2): ")
#     print("enter to c withdraw(3): ")
#     print("enter to c exit(4): ")
#     choice=int(input("enter the choice: "))
#     if choice==1:
#         balance_amt()
#     elif choice==2:
#         balance += add_amt()
#     elif choice==3:
#         balance-=withdraw()
#     else:
#         exit()        


# class employee:
#     def __init__(self,name,role):
#         self.name=name
#         self.role=role
#     def get_role(self):
#         print(f"{self.name}={self.role}")
#     @staticmethod
#     def checking(position):
#         check_pos=["manager","cook","attender"]
#         return position in check_pos
# e1=employee("dhim","manager") 
# e2=employee("yash","attender") 
# e3=employee("abhin","cook") 
# e1.get_role()
# e2.get_role()
# e3.get_role()
# print(employee.checking("manager"))

# class employee:
#     def __init__(self,name,role):
#         self.name=name
#         self.role=role
#     def get_role(self):
#         print(f"{self.name}={self.role}")
#     def __contains__(self,word):
#         return word in self.name   


# e1=employee("dhim shetty alva hegde","developer")
# print("developer" in e1)
# e2=employee("yash bandary","developer") 


# try:
#     a=int(input("enter the number:"))
#     b=int(input("enter the number:"))
#     c=a/b
#     pti
# import os
# file_path="C:/Users/Dell/Desktop/Picture1.png"
# if os.path.exists(file_path):
#     print(f"the file path {file_path} exist")
#     if os.path.isfile(file_path):
#         print("This is a file")
#     elif os.path.isdir(file_path):
#         print("This is a directory")    
# else:
#     print(f"the file path {file_path} does not exist") 
# text="hello there is file operation"
# text2="this is a file2 "
# file_path1="txttest1.txt"
# with open(file_path1,"a") as f :
#     f.write("\n"+text2)
#     print("file is created and content is inserted")  

# JSON FILES

# import json
# text2={"dhim":95,
#         "yash":100,
#         "laman":95}
# file_path="test.json"
# with open(file_path,"w") as f:
#     json.dump(text2,f,indent=4)
#     print("json file created..")

# USING CSV FILE

# import csv
# text2=[["Name","age","add"],
#        ["dhim",23,"blore"],
#        ["yash",22,"blore"]]
# file_path="testdemo.csv"
# with open(file_path,"w",newline='') as f:
#     writer=csv.writer(f)
#     for row in text2:
#         writer.writerow(row)
#     print("json file created..")

# text2="this is a file2 "
# file_path="test.json"
# with open(file_path,"w",) as f:
#     json.dump(text2,f,indent=4)
#     print("json file created..")
      
# import json      
# file_path="test.json"
# with open(file_path,"r") as f:
#     content=json.load(f)
#     print(content)
# import os
# import csv    
# file_path="testdemo.csv"
# with open(file_path,"r") as f:
#     writer=csv.reader(f)
#     for line in writer:
#         print(line)

# import datetime
# time=now.strftime("%H:%M:%S")
# print(time)
import pygame
import datetime
import time

def set_alram(set_time):
    print(f"The alram time is {set_time}")
    alram=True
    file_music="C:/Users/Dell/Desktop/Python/iphone_alarm.mp3"
    while alram:
        current_time=datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)
        
        if current_time==set_time:
            print("Lets goooo")
            pygame.mixer.init()
            pygame.mixer.music.load(file_music)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                time.sleep(1)
            alram=False
        time.sleep(1)  
        

if __name__=="__main__":
    set_time=input("Set the alram(HH:MM:SS):  ")
    set_alram(set_time)

        