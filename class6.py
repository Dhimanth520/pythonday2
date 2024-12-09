# # # def fuc():
# # #     print("hello world")
# # # fuc()
# # def sum(num1,num2):
# #     print( num1+num2)
# # def sub(num1,num2):
# #     print( num1-num2)
# # def mul(num1,num2):
# #     print(num1*num2)
# # def div(num1,num2):
# #     print( num1/num2)
# # while True:
# #     num1=int(input("enter the no: "))
# #     num2=int(input("enter the 2nd num: "))
# #     choice=int(input("click (1)add ,2(sub), 3(mul),4(div): "))
# #     if choice==1:
# #         sum(num1,num2)
# #         break
# #     elif choice==2:
# #         sub(num1,num2)
# #         break
# #     elif choice==3:
# #         mul(num1,num2)
# #         break
# #     elif choice==4:
# #         div(num1,num2)
# #         break
# #     else:
# #         print("enter a valid choice..")                

# # # res=sum(num1,num2)
# # # print(res) 
# # #    
# def fun(*lst):
#     for i in lst:
#         if i%2==0:
#             print("even",i)
#         else:
#             print("odd",i)
# lst=[1,2,3,4,5]
# fun(*lst)