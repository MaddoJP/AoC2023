f = open("input.txt", "r").read().strip()

RED_MAX = 12
GREEN_MAX = 13
BLUE_MAX = 14

value = 0
for idx, line in enumerate(f.split('\n')):
    colors = line.split(': ')[1]
    draws = colors.split('; ')
    blues, reds, greens = [], [], []
    for draw in draws:
        colorlist = draw.split(', ')
        for item in colorlist:
            number, color = item.split(' ')
            if color == 'blue':
                blues.append(int(number))
            if color == 'red':
                reds.append(int(number))
            if color == 'green':
                greens.append(int(number))
    if max(reds) <= RED_MAX and max(greens) <= GREEN_MAX and max(blues) <= BLUE_MAX:
        value += idx+1

print(value)



