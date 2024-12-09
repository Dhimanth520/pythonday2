# sets
# a={4,1,4,8,5,6,2,2,5,7,89}
# print(a)
# s=frozenset({8,96,5,2,4,1,1,5,21,5,})
# for i,x in enumerate(s):
    # print(i,x)
# s={8,96,5,2,4,1,1,5,21,5,}
# list1=list(s)
# list1.sort()
# # sorted(s)
# # set1=set(list1)
# print(set1)
# print(list1)
# fruit={"apple","bannana","orange","mango"}
# # fruit.add("chikku")
# fruit.remove("apple")
# print(fruit)
# set1={5,4,7,89,6,2,48,2,2}
# set2={6,4,7,89,5,2,1,2}
# # set3=set1.intersection(set2)
# # set3=set1.difference(set2)
# # set4=set2.difference(set1)
# print(set4)
# s1={15,48,79,56,2,154}
# s2={1,5,48,95,26,54,8}
# s3={*s1,*s2}
# print(s3)
# s=set("KanLabs")
# t=s[::-1]
# print(t)//////indexing not possible
# s={10,20,80,70,50,60}
# z=list(s)
# z.sort()
# print(z)
# set1={"dhim","abhin","abhi","yash"}
# eset=set()
# for i in set1:
#     if i[0]=="a":
#         # print("present")
#         # break
#         eset.add(i)

# print(eset) 

# eset=set()

# # no_name=int(input("enter the no: "))
# # names=input("Enter the name: ")
# while(True):
#     names=input("Enter the name: ")
#     eset.add(names)
#     z=count(eset)
#     print(z)
#     # names=input("Enter the name: ")
#     break
# print(eset)
# eset=set()
# for i in range(5):
#     name=input("enter the name: ")
#     eset.add(name)
# print(eset)   //// while loop cannot be used  only for loop cannot be used 
# import random
# eset=set()
# for i in range(11):
#     z=random.randint(15,45)
#     eset.add(z)
# print(eset)
# a={"name":"dhim","age":22,"add":"blore"}
# b={"name":"yash","age":22,"add":"mlore"}
# c={**a,**b}
# print(c)
# d={"oil":230,"clip":150,"stdu":175,"kapil":148}
# # s=dict([(1,"dhim"),(2,'pip'),(3,"pop")])
# # print(s)
# # d=sorted(d.items())
# # z=sorted(d.items(),reverse=True)
# # print(z)
# # # print(d)
# for values in d.values():
#     print(values)
# import operator
# lst=[("Dhim",12,10.55),("Aash",11,50.55)] 
# tpl=(["Dhim",12,45.55],["Aash",11,55.55])
# # i=operator.itemgetter(2)
# # print(i)
# print(sorted(lst))
# print(sorted(tpl))
# print(sorted(lst,key=operator.itemgetter(2)))
# print(sorted(tpl,key=operator.itemgetter(2)))

# d1={"mango":12,"guva":1234}
# d2={"apple":32,"pineapple":456}
# d3={"kiwi":789,"water":852}
# d4={}
# for d in (d1,d2,d3):
#     d4.update(d)
# print(d4)
# d3={1:"dim",2:"yash",3:"abhin"}
# rollno=int(input("Enter the roo number: "))
# name=d3.get(rollno)
# z=d3.values()
# print(d3.items())
# for keys in d3.keys():
#     print(f" values: {d3[values]}")
# for i in enumerate(d3.items()):
#     print(i)

# d2={4:"ratheesh"}
# d3.update(d2)
# print(d3)
# d3={1:"dim",3:"yash",2:"abhin"}
# d=sorted(d3.items())
# print(d)
# d1={"milk":25,"paste":20,"soap":50}
# d2={"milk":2,"paste":1,"soap":5}
# lst3=0
# for key in d1:
#     if key in d2:
#         print(d1[key])
#         lst3=lst3+(d1[key]*d2[key])
# print("total bill is:",lst3)

    # print(i,lst[i])




