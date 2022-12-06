from collections import Counter

with open("/Users/nicholasprice/Desktop/Development/code/advent-cal-22/day 3/day-3-data.txt", 'r') as file:
    packs = file.read()

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def badges(data):
    data = "".join(list(data)).splitlines()
    
    i = 0

    pri = 0

    while i < len(data):

        first = Counter(data[i])
        second = Counter(data[i + 1])
        third = Counter(data[i + 2])

        first_keys = list(first.keys())
        sec_keys = list(second.keys())
        third_keys = list(third.keys())

        for letter in first_keys:
            if letter in sec_keys and letter in third_keys:
                pri += (alpha.index(letter) + 1)
 
        i += 3

    print(pri)


badges(packs)