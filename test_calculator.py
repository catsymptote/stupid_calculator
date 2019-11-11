# Generate the calculator.
from generator import generate
operators = "+-*/"
a_min = -10
a_max = 10
b_min = -10
b_max = 10  
generate(operators=operators, a_min=a_min, a_max=a_max, b_min=b_min, b_max=b_max)

# Load calculator.
from calculator import *


def test_all_possible_combinations():
    # Basic calculator for testing purposes.
    def basic_calc(a, op, b):
        if op=="+":
            return a+b
        elif op=="-":
            return a-b
        elif op=="*":
            return a*b
        elif op=="/":
            if b==0:
                return None
            return a/b

    # Iterate through all possibilities.
    for a in range(a_min, a_max):
        for op in operators:
            for b in range(b_min, b_max):
                assert calc(a, op, b) == basic_calc(a, op, b)
