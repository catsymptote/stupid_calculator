def calc_answer(a, op, b):
    try:
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '*':
            return a * b
        elif op == '/':
            return a/b
        elif op == '**':
            return a**b
        elif op == '//':
            return a // b
        elif op == '%':
            return a % b
    except ZeroDivisionError:
        return None
    return None


def write_calc(a_min, a_max, b_min, b_max, operators=None):
    if operators is None:
        operators = ['+', '-', '*', '/', '**', '//', '%']

    calc_str = ''
    #calc_str += 'def user_input():\n'
    #calc_str += '\ta = int(input("a> "))\n'
    #calc_str += '\top = input("operator> ")[0]\n'
    #calc_str += '\tb = int(input("b> "))\n'
    #calc_str += '\treturn a, op, b\n\n\n'
    
    calc_str += 'def calc(a, op, b):\n'
    calc_str += '\tif op=="/" and b==0:\n'
    calc_str += '\t\treturn None\n'
    for op in operators:
        for a in range(a_min, a_max+1):
            for b in range(b_min, b_max+1):
                calc_str += f'\tif a=={a} and op=="{op}" and b=={b}:\n'
                calc_str += f'\t\treturn {calc_answer(a, op, b)}\n'.format(a, op, b)


    f = open('calculator.py', 'w')
    f.write(calc_str)
    f.close()


def generate(a_min=-10, a_max=10, b_min=-10, b_max=10, operators=None):
    write_calc(a_min, a_max, b_min, b_max, operators)


if __name__ == '__main__':
    generate()
