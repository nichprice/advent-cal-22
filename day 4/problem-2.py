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

        overlap = False
        
        for i in range(min(nums), max(nums) + 1):
            if i >= min(first) and i >= min(second) and i <= max(first) and i <= max(second):
                overlap = True
        
        if overlap == True:
            ans += 1

        print(nums)
        print(f'{first} {second} {ans}')


overlap(groups)