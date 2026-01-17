with open('input') as f:
     = [int(x) for x in next(f)] # read first line
    array = []
    for line in f: # read rest of lines
        array.append([int(x) for x in line.split()])