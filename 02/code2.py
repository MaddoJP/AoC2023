f = open("input.txt", "r").read().strip()

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
            elif color == 'red':
                reds.append(int(number))
            elif color == 'green':
                greens.append(int(number))
    value +=max(reds)*max(greens)*max(blues)

print(value)



