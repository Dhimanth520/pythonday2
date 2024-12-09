def sum(num):
    if num==0:
        return 0
    else:
        return num +sum(num-1)
    # return num sum(num+1)
    # add=add+num
    # print(num)
    # sum(num-1)
    # print(add)
    # for x in range(1,num+1):
res=sum(10)
print(res)
# print(res)
