with open("/Users/nicholasprice/Desktop/Development/code/advent-cal-22/day 4/day-4-data.txt", 'r') as file:
    groups = file.read()


def overlap(data):
    data = "".join(list(data)).splitlines()

    ans = 0 

    for i in range(len(data)):

        nums = []
        num = []
        for j in range(len(data[i])):
            if data[i][j] != '-' and data[i][j] != ',':
                num.append(data[i][j])
            else:
                nums.append(num)
                num = []
        nums.append(num)
        

        for a in range(len(nums)):
            nums[a] = int(''.join(nums[a]))



        first = [nums[0], nums[1]]
        second = [nums[2], nums[3]]

        if min(first) <= min(second) and max(first) >= max(second):
            ans += 1
        elif min(second) <= min(first) and max(second) >= max(first):
            ans += 1

        print(f'{first} {second} {ans}')


overlap(groups)