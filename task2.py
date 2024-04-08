#! python3
# Find the volume of a sphere.
# You will ask the user to enter the radius of the sphere.
# Calculate the Volume and then display the result to the user.
# You will need to import the math module in order to use math.pi

# Inputs:
# radius
#
# Outputs
# volume
#
# test output radius of 3 should give volume of 113.09733552923254

import math

r = input("Enter the radius of a random sphere :")

r = int(r) 
pi = math.pi
r3 = math.pow(r,3)

answer = 4/3 * pi * r3

print(answer)
