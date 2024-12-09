# user_name=input("enter the user name: ")
# passwored=input("enter the password: ")
# demo_name="dhim"
# demo_pass="1234"
# lst1=[]
# while(True):
#     user_name=input("enter the user name: ")
#     passwored=input("enter the password: ")
#     if user_name==demo_name and passwored==demo_pass:
#         print("welcome")
#         break
#     else:
#         # print("invalid user name or password")
#         passwored.append(lst1)
#         # for x in lst1:
#         while True:
#             if x==passwored:
#                 print("this invalid pass alredy exist")
#                 print(x)
#                 break
#         print("invalid user name or pass")        
# # list1=[]
# # list1.append("yash")
# # print(list1)
# passwords=[]
# passs="DEMO"
# while True:
#     password=input("Enter password: ")
#     if password==passs:
#         print("welcome")
#         break
#     elif password in passwords:
#         print("You made the same mistake")
#     else:
#         passwords.append(password)
# list1=["anil","ashok","amol","adithya","dhim"]
# list1.insert(1,"yash")
# list1.append("zolo")
# list1.remove("amol")
# list1[1]="hello"
# list1.sort()
# list1.sort(reverse=True)
# print(list1)

# 6,7,8,9,10
# # print(lst3)
# # print(lst4)
# # print(len(lst4))
# lst3.clear()
# # print(lst3)

# # del lst2
# # print(lst2)
# # lst2[2:4]=[100,200,300]

# print(lst2[2:])
# lst2[2:]=[100,200,300]
# print(lst2)
# lst2[-1]=100
# lst2[-2]=200
# lst2[-3]=300
# print(lst2)

# d1=[1,2,3,4,5,6,7,8,9,10]
# for i in d1:
# k=[100,200,300]
# # z=len(d1)
# for i in len(d1):
#     d1.append(k)
# print(d1)
# for i in range(len(d1)):
# k=[100,200,300]

# d1.pop()
# d1.pop()
# d1.pop()
# d1.append(k)
# print(d1)

# d1.reverse()
# print("before reversing",d1)
# d1[:3]=[100,200,300]
# print(d1)
# d1.reverse()
# print(d1)
# lst1=[]
# # while(user_in<=5):

# # user_in=int(input("enter the number: "))
# while(len(lst1)<=5):
#     user_in=int(input("enter the number: "))
#     lst1.append(user_in)
#     # if len(lst1)==5:
#         # break
#     # user_in=int(input("enter the number: "))
# print(lst1)

# 1

# lst1=[1,3,7,5,9,11,13,15]
# lst2=[2,8,6,10]
# # lst1.insert(3,lst2)
# lst1[3]=lst2
# for i in range(lst1)
# print(lst1)
# lst1.sort()
# print(lst1)

# print(lst1)

# lst1.sort()
# print(lst1)
# lst1=["dhim","yash","abhin","abhay"]
# lst2=[]
# for x in lst1:
#    z=x.upper()
#    z.append(last2)
# print(lst2)

# 2
# d1=[]
# d1.append(1)
# d1.append(2)
# d1.append(3)
# d1.append(4)
# d1.append(5)
# print(d1)
# d1.pop()
# d1.pop()
# print(d1)

# lst=[100,150,400]
# lst2=[]
# for x in lst:
#     C=(x-32)*5/9
#     lst2.append(C)
# print(lst2)

# lst=[1,2,-10,3,-7,-5,-6]
# pos=[]
# neg=[]
# for x in lst:
#     if x>0:
#         pos.append(x)
#     else:
#         neg.append(x)    
# print(pos)
# print(neg)


# # import operator
# # lst=[("Dhim",12,10.55),("Aash",11,50.55)] 
# # tpl=(["Dhim",12,45.55],["Aash",11,55.55])
# # # i=operator.itemgetter(2)
# # # print(i)
# # print(sorted(lst))
# # print(sorted(tpl))
# # print(sorted(lst,key=operator.itemgetter(2)))
# # print(sorted(tpl,key=operator.itemgetter(2)))
# lst=[(1,2,3),(4,5,6),(7,8)]

# res=divmod(17,3)
# print(res)
# names=["shila","sushala",("dhim",),("yash",),"girl1",("boy1",),"sujatha"]
# bois=0
# girls=0
# for name in names:
#     if isinstance(name,tuple):
#         bois+=1       
#     else:
#         girls+=1
# print(bois)
# print(girls)

# lst=[("dhim",1,12),("yash",2,12),("abhin",3,12)]
# lst2=[]
# for x in lst:
#     # print(x)
#     lst2.append(x[0])
# print(lst2)

#    lst2=lst2+[x[0]] // this is not possible
# print(lst2)

# tpl=('q','w','e','r','t','y')
# print(tpl)
# print(type(tpl))
# z=str(tpl)
# print(z)
# # print(type(z))
# x=' '.join(tpl)
# print(type(x))
# print(x)
# z=tpl[0:3]
# for i,ele in enumerate(tpl):
    # print(i,ele)
# index=tpl[0:]
# print(index)
# for i,index in range(len(tpl)):
#     print(i,index)
# print(z)
# for i in range(len(tpl)):
    # print(i,tpl[i])


share_name=("tata","infosys","voltas","mahindra")
d_o_p=(1/4/202,2/3/24,4/3/2024)
# cost_price=(1000,1200,900,950)
cost_price=(5100,2000,500,1800)
no_shares=(5,3,7,9)
# selling_price=(1100,2000,500,1800)
selling_price=(1000,500,900,950)
# total cost of portpholio
total_cost=0
for i in range(len(cost_price)):
    total_cost=total_cost+(cost_price[i]*no_shares[i])
print("Total cost of the portpholio: ",total_cost)
print("-----------------------")
# selling price
total_selling_price=0
for i in range (len(selling_price)):
    total_selling_price=total_selling_price+(selling_price[i]*no_shares[i])
print("selling price: ",total_selling_price)
#prifit or loss
if total_selling_price>total_cost:
    profit=total_selling_price-total_cost
    percentage_profit=profit/100
    print("Profit: ",profit)
    print(f"profit percent is: {percentage_profit}%" )
else:
    loss=total_cost-total_selling_price
    loss_percent=loss/100
    print("loss: ",loss)
    print(f"loss percent is: {loss_percent}")
