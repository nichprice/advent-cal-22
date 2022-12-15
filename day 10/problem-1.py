with open("/Users/nicholasprice/Desktop/Development/code/advent-cal-22/day 10/data.txt", 'r') as file:
    instr = [line.strip() for line in file]

# with open("/Users/nicholasprice/Desktop/Development/code/advent-cal-22/day 10/dummy.txt", 'r') as file:
#     dummy = [line.strip() for line in file]


def radio(data):

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
            j += 2
            for k in range(j, len(vals)):
                vals[k][0] += val
        else:
            j += 1

    print(vals)

    signals = []

    signals.append(vals[19][0] * 20)
    signals.append(vals[59][0] * 60)
    signals.append(vals[99][0] * 100)
    signals.append(vals[139][0] * 140)
    signals.append(vals[179][0] * 180)
    signals.append(vals[219][0] * 220)

    print(sum(signals))


radio(instr)