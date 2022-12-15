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

    scores = []

    for i in range(1, len(map) - 1):
        for j in range(1, len(map[0]) - 1):
            x = map[i][j]

            left = list(map[i][:j])
            right = list(map[i][(j + 1):])
            above = []
            below = []

            for k in range(i):
                above.append(map[k][j])
            
            for l in range(i + 1, len(map)):
                below.append(map[l][j])

            r_score = 0
            l_score = 0 
            a_score = 0
            b_score = 0
            
            if len(above) > 1:
                above.reverse()
            if len(left) > 1:
                left.reverse()

            for num in left:
                if num < x:
                    l_score += 1
                else:
                    l_score += 1
                    break

            for num in right:
                if num < x:
                    r_score += 1
                else:
                    r_score += 1
                    break
            
            for num in above:
                if num < x:
                    a_score += 1
                else:
                    a_score += 1
                    break

            for num in below:
                if num < x:
                    b_score += 1
                else:
                    b_score += 1
                    break
            
            score = l_score * r_score * a_score * b_score
            
            scores.append(score)

    print(max(scores))

looker(trees)