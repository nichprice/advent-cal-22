with open("/Users/nicholasprice/Desktop/Development/code/advent-cal-22/day 5/moves.txt", 'r') as file:
    lines = file.read()

    stacks = [
    ['B','Q','C'],
    ['R','Q','W','Z'],
    ['B','M','R','L','V'],
    ['C','Z','H','V','T','W'],
    ['D','Z','H','B','N','V','G'],
    ['H','N','P','C','J','F','V','Q'],
    ['D','G','T','R','W','Z','S'],
    ['C','G','M','N','B','W','Z','P'],
    ['N','J','B','M','W','Q','F','P'],
    ]

def stacker(data):
    data = "".join(list(data)).splitlines()

    for line in data:
        t = int(line[-1]) - 1
        f = int(line[-6]) - 1

        if len(line) == 18:
            m = int(line[5])
        else:
            m = int(f'{line[5]}'+f'{line[6]}')

        temp = stacks[f][-m:]

        for num in temp:
            stacks[t].append(num)
            stacks[f].pop(-1)

    ans = ''
    
    for i in range(len(stacks)):
        ans += stacks[i][-1]

    print(ans)

stacker(lines)