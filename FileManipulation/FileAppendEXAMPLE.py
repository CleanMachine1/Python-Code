#!/usr/bin/python3

f = open ("data.txt", "a")
var1 = str(input("Enter a line to add to data.txt"))
f.write(var1)
f.close()