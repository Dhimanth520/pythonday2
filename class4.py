# def check(input_name,input_pass):
#     user_name="dhim"
#     password= 1234 
#     if input_name==user_name and input_pass==password:
#         print("permited")
#     else:
#         print("not permited")

# # check(input_name,input_pass)
# input_name=input("enter the user name: ")
# input_pass=int(input("enter the user password: "))
# check(input_name,input_pass)

def even(*input_no):
    # print(type(input_no))
    for i in input_no:
        # print(type(i))
        if i % 2==0:
            print("even",i)
        else:
            print("oddd",i) 

# input_no=int(input("enter the number: "))  
input_no=[1,2,3,4,5]   
even(*input_no) 



# def check(*user):
#     for char in user:
#         if "@gmail.com" in char:
#             print("valid emial")
#         else:
#             print("not vaild")

# user=input("enter the enamil: ")
# check(user)