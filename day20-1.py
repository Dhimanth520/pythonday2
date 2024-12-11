room_numbers=[101,105]
cost_room=5000
total_cost_veg=cost_room+1000
total_cost_non_veg=cost_room+2000
amt_paid=[]
def checkin():
    room=int(input("Enter the room number: "))
    if room in room_numbers:
        print("room already alloted..")
        
    else:
        print("room booked successfully..")
        print("the cost per night si 5000")
        room_numbers.append(room)
def payment():                
    print("enter the amount to be paid: ",amt_paid)
    # while True:
    user_amount=int(input("Pay: "))
    for x in amt_paid:
        if user_amount==x:
            print("Payment successfull....")
            break
        else:
            print("Please try again to pay...")        
def checkout():
    global room_numbers,cost_room,total_cost_non_veg,total_cost_veg,amt_paid
    while True:
        room_out=int(input("Enter the room to be checked out: "))
        if room_out in room_numbers:
            room_numbers.remove(room_out)
            ask_meals=int(input("Did u inclue the meals: 1(s) and 2(no): "))
            if ask_meals==1:
                type_meal=int(input("enter 1 for veg and 2 for non-veg: "))
                if type_meal==1:
                    amt_paid.append(total_cost_veg)
                    print("The total cost of stay + veg meal will be: ")
                    print(f"the amount to be paid is :{total_cost_veg}")
                    break
                else:
                    amt_paid.append(total_cost_non_veg)
                    print("The total cost of stay + non-veg meal will be: ")
                    print(f"the amount to be paid is :{total_cost_non_veg}")
                    break
            else:
                print("cost of only stay is: ",cost_room)
                break
    payment()    
if __name__=="__main__":        
    while True:
        choice=int(input("do u want yo checkin(1) or checkout(2) or exit:"))
        if choice==1:
            checkin()
        elif choice==2:
            checkout()   
        else:
            break