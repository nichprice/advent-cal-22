from collections import Counter

with open("/Users/nicholasprice/Desktop/Development/code/advent-cal-22/day 3/day-3-data.txt", 'r') as file:
    packs = file.read()

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']



def prioritize(data):
    items = "".join(list(data)).splitlines()

    pri = 0

    for i in range(len(items)):
        first = items[i][:(len(items[i])//2)]
        second = items[i][(len(items[i])//2):]

        onecount = Counter(first)
        twocount = Counter(second)

        onekeys = list(onecount.keys())
        twokeys = list(twocount.keys())

        for a in range(len(onekeys)):
            for b in range(len(twokeys)):
                if onekeys[a] == twokeys[b]:
                    letter = onekeys[a]
                    pri += alpha.index(letter) + 1
    print(pri)


prioritize(packs)