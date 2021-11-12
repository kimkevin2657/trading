import glob
import json

import itertools




temp = 1.0 - abs(2755.0 - 2660.0)/2306.495

temp2 = 1.0 - abs(740500.0 - 715700.0)/383708.135

temp3 = 1.0 - abs(66881000.0 - 62277000.0)/48099185.707

temp4 = 1.0 - abs(0.0 - 0.0)/0.009439

temp5 = 1.0 - abs(0.000675656 - (-1.0*0.00111653))/0.008878

temp6 = 1.0 - abs(0.0002392 - (-1.0*0.0002087))/0.005271

print(abs(0.000675656 - (-1.0*0.00111653)))
print(0.008878)

print()

print(temp)
print(temp2)
print(temp3)
print(temp4)
print(temp5)
print(temp6)
print((temp+temp2+temp3+temp4+temp5+temp6)/(6.0))




"""
temp = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]


if isinstance(temp, list):
    print("hit")
else:
    print("no")

print(len(temp))

lenval = int(float(len(temp))/5.0)

tempidx = []
for i in range(0, len(temp)):
    if i == 0:
        tempidx.append(i)
    else:
        if i % lenval == 0:
            tempidx.append(i)

print(tempidx)

"""