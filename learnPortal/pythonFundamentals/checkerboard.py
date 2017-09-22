''' This program prints out a checkerboard pattern '''

size = 8

for i in range(0, size):
    row = '' #resets the row each time
    for j in range(0, size):
        if i%2 is j%2:
            row += '*'
        else:
            row += ' '
    print row
