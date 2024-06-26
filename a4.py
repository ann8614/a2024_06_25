import math
import pyinputplus as pyip
a = pyip.inputNum('請輸入對邊',min = 0 ,max =100)
b = pyip.inputNum('請輸入斜邊',min = 0 ,max =100)
r = math.asin(a / b)
d = math.degrees(r)
print(f"對邊:{a},斜邊:{b},角度:{round(d,ndigits=2)}" )