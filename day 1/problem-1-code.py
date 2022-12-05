with open("/Users/nicholasprice/Desktop/Development/code/advent-cal-22/day 1/problem-1-data.txt", 'r') as file:
    cals = file.read()

print(cals)

def cal_math(data):
    nums = "".join(list(data)).splitlines()
    elves = []
    elf = []

    for i in range(len(nums)):
        if nums[i] != '':
            elf.append(int(nums[i]))
        else:
            elves.append(elf)
            elf = []

    elves.append(elf)
    
    for i in range(len(elves)):
        elves[i] = sum(elves[i])

    print(max(elves))


cal_math(cals)

