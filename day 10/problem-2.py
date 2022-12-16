with open("/Users/nicholasprice/Desktop/Development/code/advent-cal-22/day 10/data.txt", 'r') as file:
    instr = [line.strip() for line in file]

# with open("/Users/nicholasprice/Desktop/Development/code/advent-cal-22/day 10/dummy.txt", 'r') as file:
#     dummy = [line.strip() for line in file]


def radio(data):

    steps = []
    vals = []
    
    for i in range(len(data)):
        if data[i][0] == 'a':
            vals.append([1])
            vals.append([1])
        else:
            vals.append([1])

    j = 0
    for i in range(len(data)):
        if data[i][0] == 'a':
            val = int(data[i][5:])
            steps.append(val)
            j += 2
            for k in range(j, len(vals)):
                vals[k][0] += val
        else:
            steps.append('x')
            j += 1

    print(f'steps =\n {steps} \n \nvals =\n {vals}')

    for step in steps:
        if step



radio(instr)