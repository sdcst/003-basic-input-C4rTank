#! python3
#
# Find the radius of a sphere if you are given the volume.
# Think about how you would need to solve this equation if you were doing it on paper
#
# Inputs:
# Volume (float)
#
# Outputs:
# radius (float)
#
# Test output Volume of 20.22 should give radius of:1.69002229118
# Note: You will need to do some strange things with your cube root.
# Remember that a cube root is the same as an exponent of 1/3, but
# here you will need to do a power of 1.0/3 or something strange happens.

import math

v = input("Pick a number for Volume :")

v = float(v)

pi = math.pi

st1 = 3 * v
st2 = 4 * pi
st3 = st1 /st2

answer = st3**1/3

print("The radius of your sphere is", answer)

