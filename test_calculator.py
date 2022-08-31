# Generate the calculator.
from generator import generate
operators = "+-*/"
a_min = -10
a_max = 10
b_min = -10
b_max = 10  
# generate(operators=operators, a_min=a_min, a_max=a_max, b_min=b_min, b_max=b_max)
generate()

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
        elif op=="**":
            if a==0 and b<0:
                return None
            return a**b
        elif op=='//':
            return a//b
        elif op=='%':
            return a%b

    # Iterate through all possibilities.
    for a in range(a_min, a_max):
        for op in operators:
            for b in range(b_min, b_max):
                expected = basic_calc(a, op, b)
                received = calc(a, op, b)
                # assert expected * 0.999 < received < expected * 1.001
                assert expected == received, f'{expected} =/= {received}'
    return True


if __name__ == '__main__':
    if test_all_possible_combinations():
        print('Tests ran successfully!')
