class employee:
    def __init__(self,name,age,addr):
        self.name=name
        self.age=age
        self.addr=addr
    def get_data(self):
        return self.name,self.age,self.addr
e1=employee("dhim",23,"banglore")  
# e1.set_data("dhim",23,"banglore") 
print(list(e1.get_data())    )     