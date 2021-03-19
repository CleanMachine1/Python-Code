#!/usr/bin/python3

f = open ("data.txt", "w")
var1 = str(input("Enter a line to write to data.txt"))
f.write(var1)
f.close()