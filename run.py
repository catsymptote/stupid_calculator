from generator import generate
generate()

from calculator import calc
a = int(float(input("a> ")))
op = input("operator> ")
b = int(float(input("b> ")))

print(calc(a, op, b))
