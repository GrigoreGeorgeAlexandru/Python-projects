def is_monotone_x(points: list )->bool:
    local_min = 0
    for i in range(len(points)):
        if points[i][0]<points[(i+1) % len(points)][0] and  points[i][0] < points[(i-1) % len(points)][0]:
            local_min += 1
    return(local_min == 1)

def is_monotone_y(points: list )->bool:
    local_min = 0
    for i in range(len(points)):
        if points[i][1]>points[(i+1) % len(points)][1] and  points[i][1] > points[(i-1) % len(points)][1]:
            local_min += 1
    return(local_min == 1)

with open("2_in.txt") as f:
        nr=int(f.readline())
        for t in range(nr):
            nr2=int(f.readline())
            polygon=[[int(j) for j in next(f).strip('\n').split(' ')] for x in range(nr2)]
            print(is_monotone_x(polygon))
            print(is_monotone_y(polygon))
