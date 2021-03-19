#!/usr/bin/python3

f = open("data.txt", "r")
var1 = f.read()
if var1 == "1":
    print("The data inside of data.txt == '1'")
elif var1 == "2":
    print("the data inside of data.txt == '2'")
else:
    print("unknown value")

f.close()
