# # print(int(3/4))
# # b=3*(1+2j)
# # print(b.conjugate())


# # print(divmod(17,3))

# # print(17//3)
# # print(17%3)
# import math
# # print(math.log10(12))
# print(math.trunc(5.8956))
# print(math.ceil(5.2557))
# msg="hello"
# x="-".join(msg)
# print(x)
# # import random
# # import datetime
# # # print(random.seed(datetime.time()))
# # import math
# # a=-2.8
# # b=-0.5
# # c=0.2
# # print(math.trunc(a))
# # print(math.ceil(a))
# # a="Hello World"
# # print(a.swapcase())
# # print(ord('A'))
# # print(ord('a'))
# # print(chr(76))
# # print(chr(97))
# # REGEX FUNCTION 
# import re

# txt="The raim in mangalore"
# x=re.findall("rain",txt)
# print(x)
# # x=re.sub(" ","-",txt)
# # # print(x)
# # y=re.split(" ",txt)
# # print(y)
# # a="hello"
# # b="hello"
# # print(id(a), id(b))
# # a="Bamboozled"
# # print(a[0],a[1])
# # print(a[0:5])
# # msg="keep yourself warm"
# # print(msg[0:-2])
# # msg="khfnbdbhd bhbdf"
# # print(msg[1:8])  # prints "hhfnb"  # prints "hh
# # print(msg[1:8:2])
import logging

logging.basicConfig(level=logging.INFO,filename="test.txt",filemode="w",format="%(asctime)s - %(levelname)s - %(message)s")

# # logging.debug("debug")


# # x=2
# # logging.info(f"The value of  x is {x}")
# # # logging.warning("warrning")
# # # logging.error("error")
# # # logging.critical("criticaal")

# # logging stack trace
# # try:
# #     1/0
# # except ZeroDivisionError as e:
# #     logging.exception("Zero division error")


# # custom loggers
logger=logging.getLogger("name1")
handler=logging.FileHandler("test_content3.txt")
Formatter=logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(Formatter)
logger.addHandler(handler)
logger.info("New custom logger now")
# # print(abs(-8.56))
# num=int(input("ENter the munber: "))
# if num%2==0:
#     print("even num",num)
# else:
#     print("the number is odd: ",num)
     