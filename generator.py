def write_calc(operators, a_min, a_max, b_min, b_max):
    calc_str = ""
    #calc_str += 'def user_input():\n'
    #calc_str += '\ta = int(input("a> "))\n'
    #calc_str += '\top = input("operator> ")[0]\n'
    #calc_str += '\tb = int(input("b> "))\n'
    #calc_str += '\treturn a, op, b\n\n\n'
    
    calc_str += "def calc(a, op, b):\n"
    calc_str += '\tif op=="/" and b==0:\n'
    calc_str += '\t\treturn None\n'
    for op in operators:
        for a in range(a_min, a_max):
            for b in range(b_min, b_max):
                if not(op=="/" and b==0):
                    calc_str += '\tif a=={0} and op=="{1}" and b=={2}:\n'.format(a, op, b)
                    calc_str += '\t\treturn {0}{1}{2}\n'.format(a, op, b)


    f = open('calculator.py', 'w')
    f.write(calc_str)
    f.close()

def generate(operators="+-*/", a_min=-10, a_max=10, b_min=-10, b_max=10):
    write_calc(operators, a_min, a_max, b_min, b_max)
