#!/usr/bin/python3.7

radius = float(input("What is the radius of the circle?"))
area = 3.14159 * (radius ** 2)
circumference = 3.14159 * (radius * 2)

print("Enter given angle to calculate sectors")
print("If the circle is a full circle please provide 360")
deg = float(input())

if deg == 360:
    print("The Area of the circle =", area)
    print("The Circumference of the circle =", circumference)

elif deg < 360:
    sarea = (deg / 360) * area 
    scircumference = (deg / 360) * circumference + radius + radius
    print("The Area of the circle =", sarea)
    print("The Circumference of the circle =", scircumference)

else:
    print("Invalid")
