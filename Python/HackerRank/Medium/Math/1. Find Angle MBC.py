# https://www.hackerrank.com/challenges/find-angle/problem

# '\u00b0'      For dislplaying degree
# '\u00b0 F'    For displaying degree F
import math
ab = int(input())
bc = int(input())

ac = math.sqrt(ab**2 + bc**2)
mc = ac/2

angle_acb = math.asin(ab/ac)
angle_mbc = math.degrees(math.pi/2 - angle_acb)

print(str(round(angle_mbc))+ '\u00b0')