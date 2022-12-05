with open("/Users/nicholasprice/Desktop/Development/code/advent-cal-22/day-2-data.txt", 'r') as file:
    games = file.read()

def score_machine(data):
    rounds = "".join(list(data)).splitlines()
    print(rounds)

    points = 0

    print(rounds[1])

    for i in range(len(rounds)):
        if rounds[i][2] == "X":
            points += 1
            if rounds[i][0] == "A":
                points += 3
            elif rounds[i][0] == "C":
                points += 6

        elif rounds[i][2] == "Y":
            points += 2
            if rounds[i][0] == "A":
                points += 6
            elif rounds[i][0] == "B":
                points += 3  

        elif rounds[i][2] == "Z":
            points += 3
            if rounds[i][0] == "B":
                points += 6
            elif rounds[i][0] == "C":
                points += 3

    print(points)



score_machine(games)