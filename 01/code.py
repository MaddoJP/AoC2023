f = open("input2.txt", "r").read().strip()
total_sum = 0
for line in f.split('\n'):
    nums = []
    current_sum = 0
    for char in line:
        if char.isdigit():
            nums.append(char)
    current_sum = "" + nums[0] + nums[-1]
    total_sum += int(current_sum)

print(total_sum)
