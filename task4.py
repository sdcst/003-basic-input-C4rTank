#! python3
#
# Surface area of a cone
# Find the surface area of a cone given the height and the radius.
# You will need to ask the user to enter in both variables, and will 
# need to use the Pythagorean relationship to find the slant height. 
# (2 points)
#
# Inputs:
# height, radius
#
# Outputs:
# surface area
#
# Test output
# r = 3
# h = 5
# sa = 83.2297607912

import math

h = input("Pick a number for height :")
r = input("Pick a number for radius :")

h = int(h) 
r = int(r)
pi = math.pi

h2 = h * h
r2 = r * r


sqrt = math.sqrt(h2 + r2)

s1 = pi * r
s2 = r + sqrt
answer = s1 * s2

print("The surface area of your cone is", answer)
