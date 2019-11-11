operators = "+-*/"
a_max = 100
b_max = 100
operators = "+-*/"


calc_str = 'a = int(input("a> "))\n'
calc_str += 'op = input("operator> ")[0]\n'
calc_str += 'b = int(input("b> "))\n\n'

#calc_str += 'if op=="/" and b==0:\n'
#calc_str += '\tprint("Dividing by 0 is bad, mkay!")\n'

for op in operators:
    for a in range(a_max):
        for b in range(b_max):
            if not(op=="/" and b==0):
                calc_str += 'if a=={0} and op=="{1}" and b=={2}:\n'.format(a, op, b)
                calc_str += '\tprint({0}{1}{2})\n'.format(a, op, b)

#calc_str += 'else:\n'
#calc_str += '\tprint("Invalid input .. (probably.)")\n'

f = open('calculator.py', 'w')
f.write(calc_str)
f.close()
