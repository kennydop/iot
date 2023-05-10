with open('adc.txt', 'r') as f:
    lines = f.readlines()
    for x in range(256):
        y = 15.81*x - 135.5
        print('x:', x, 'y0:', lines[x].strip(), 'y', y)