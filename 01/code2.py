f = open("input2.txt", "r").read().strip()
total_sum = 0
for line in f.split('\n'):
    nums = []
    for i, c in enumerate(line):
        if c.isdigit():
            nums.append(c)
        for d, val in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
            if line[i:].startswith(val):
                nums.append(str(d+1))
    current_sum = int(digits[0]+digits[-1])
    total_sum += current_sum
print(total_sum)