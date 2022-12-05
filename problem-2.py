with open("/Users/nicholasprice/Desktop/Development/code/advent-cal-22/day-2-data.txt", 'r') as file:
    games = file.read()

def score_machine(data):
    rounds = "".join(list(data)).splitlines()
    
    points = 0

    for i in range(len(rounds)):
        if rounds[i][2] == "X":
            if rounds[i][0] == "A":
                points += 3
            elif rounds[i][0] == "B":
                points += 1
            elif rounds[i][0] == "C":
                points += 2
        
        elif rounds[i][2] == "Y":
            points += 3
            if rounds[i][0] == "A":
                points += 1
            elif rounds[i][0] == "B":
                points += 2
            elif rounds[i][0] == "C":
                points += 3

        
        elif rounds[i][2] == "Z":
            points += 6
            if rounds[i][0] == "A":
                points += 2
            elif rounds[i][0] == "B":
                points += 3
            elif rounds[i][0] == "C":
                points += 1

    print(points)


score_machine(games)