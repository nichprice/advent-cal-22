with open("/Users/nicholasprice/Desktop/Development/code/advent-cal-22/day 8/trees.txt", 'r') as file:
    trees = [line.strip() for line in file]


def looker(data):

    map = []

    for string in data:
        row = []
        for number in string:
            row.append(int(number))

        map.append(row)

    vis = ((len(map) - 2) * 2) + ((len(map[0]) - 2)*2) + 4


    for i in range(1, len(map) - 1):
        for j in range(1, len(map[0]) - 1):
            x = map[i][j]

            left = map[i][:j]
            right = map[i][(j + 1):]
            above = []
            below = []

            for k in range(i):
                above.append(map[k][j])
            
            for l in range(i + 1, len(map)):
                below.append(map[l][j])

            print(f'i = {i}, j = {j}')
            print(f'map[i][j] = {map[i][j]}')
            print(f'left = {left}')
            print(f'right = {right}')
            print(f'above = {above}')
            print(f'below = {below}')

            if x > max(left) or x > max(right) or x > max(above) or x > max(below):
                vis += 1
    
    print(vis)


looker(trees)