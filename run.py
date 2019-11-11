from generator import generate
generate()

from calculator import *
a = int(input("a> "))
op = input("operator> ")[0]
b = int(input("b> "))

print(calc(a, op, b))
