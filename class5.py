# def cityname(*city):
#     print(city)
# # #     # lst=[]
# # #     # i=0
# # #     # # name=input("enter the name of the city: ")
# # #     # while True:
# # #     #     name=input("enter the name of the city: ")
# # #     #     lst.append(name)
# # #     #     i+=1
# # #     #     if i>=10:
# # #     #         print(lst)
# # #     #         break
# # #         # if len(lst)<=10:
# # #             # break
# # #     # print(name)

# # name=input("enter the name of the city: ")
# city=[]
# no_city=int(input("enter the no of the city: "))
# for i in range(no_city):
#     city_name=input("enter the city name: ")
#     city.append(city_name)
# cityname(*city)



# # task2
# # # print("Do u want to CheckIN(1) or CheckOUT(2): ")
# # # user=int(input("Enter the Choice: "))
# # # if user==1:
# # #     checkin()
# # # elif user==2:
# # #     checkout()
# # # else:
# # #     print("Enter a valid choice....")        
roomnumber=[101,105]
def checkin():
    while True:
        # no_rooms=int(input("Enter the number of rooms needed: "))
        # for i in range()
        room_no=int(input("Enter the room no: "))
        # roomnumber.append(room_no)
        # print(roomnumber)
        if room_no in roomnumber:
            print("Room not avaliable...")
        else:
            roomnumber.append(room_no)
            print("Room avaliable")
            break
# checkin()     
def checkout():
    room_out=int(input("Enter the room number to check out: "))
    while True:
        if room_out in roomnumber:
            roomnumber.remove(room_out)
            print("Checked out successfully...")
            break  
        else:
            print("room is not occupied..")
            break     
# checkout()  
while True:
    print("Do u want to CheckIN(1) or CheckOUT(2) or Exit(3): ")
    user=int(input("Enter the Choice: "))
    if user==1:
        checkin()
    elif user==2:
        checkout()
    elif user==3:
        print("thanku.....") 
        break   
    else:
        print("Enter a valid choice....")       

